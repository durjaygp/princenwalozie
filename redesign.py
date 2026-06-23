import os
import re
import glob

# Files to update
files = glob.glob('d:/other/princenwalozie/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Font
    content = content.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'
    )
    content = content.replace("'Outfit'", "'Plus Jakarta Sans'")
    content = content.replace('"Outfit"', "'Plus Jakarta Sans'")
    
    # 2. Shadows (Make brutalist)
    content = re.sub(r'shadow-\[[^\]]+rgba\((16,185,129|59,130,246),0\.[12][50]?\)\]', r'shadow-[4px_4px_0px_#111827] dark:shadow-[4px_4px_0px_#10B981]', content)
    content = re.sub(r'hover:shadow-\[[^\]]+rgba\((16,185,129|59,130,246),0\.[23][50]?\)\]', r'hover:shadow-[8px_8px_0px_#111827] dark:hover:shadow-[8px_8px_0px_#10B981]', content)

    # 3. Unrounding
    content = re.sub(r'\brounded-(?:sm|md|lg|xl|2xl|3xl)\b', 'rounded-none', content)
    content = re.sub(r'\brounded\b', 'rounded-none', content)
    # Special fix for the profile picture which had `rounded-2xl`
    content = content.replace('rounded-none shadow-2xl', 'rounded-none shadow-[8px_8px_0px_#111827] dark:shadow-[8px_8px_0px_#10B981] border-2 border-gray-900 dark:border-white')
    
    # 4. Containers Outlines
    # The existing borders are border border-primary/20
    # Let's change them to border-2 border-gray-900 dark:border-white
    content = content.replace('border border-primary/20', 'border-2 border-gray-900 dark:border-gray-700')
    content = content.replace('hover:border-primary/50', 'hover:border-primary dark:hover:border-primary')
    content = content.replace('border border-primary/10', 'border-2 border-gray-900 dark:border-gray-700')
    content = content.replace('hover:border-primary/30', 'hover:border-primary dark:hover:border-primary')
    
    # Clean up navbar blurring for brutalism, maybe? I'll keep the blur, but give it a sharp bottom border
    content = content.replace('border-t border-gray-200', 'border-t-2 border-gray-900 dark:border-gray-700')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Redesign applied.")
