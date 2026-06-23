import glob
import re

# 1. Fix broken classes
files = glob.glob('d:/other/princenwalozie/*.html')
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix regex mistakes from previous script
    content = content.replace('rounded-none-none', 'rounded-none')
    content = content.replace('rounded-none-full', 'rounded-none') # keeping it brutalist
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Reorder sections in index.html
with open('d:/other/princenwalozie/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract sections using regex
experience_match = re.search(r'(<!-- EXPERIENCE START -->.*?<!-- EXPERIENCE END -->)', content, re.DOTALL)
toolkit_match = re.search(r'(<!-- TOOLKIT START -->.*?<!-- TOOLKIT END -->)', content, re.DOTALL)
awards_match = re.search(r'(<!-- CERTIFICATIONS & AWARDS FULL START -->.*?<!-- CERTIFICATIONS & AWARDS FULL END -->)', content, re.DOTALL)
leadership_match = re.search(r'(<!-- LEADERSHIP START -->.*?<!-- LEADERSHIP END -->)', content, re.DOTALL)
testimonials_match = re.search(r'(<!-- RECOMMENDATIONS/TESTIMONIALS START -->.*?<!-- RECOMMENDATIONS/TESTIMONIALS END -->)', content, re.DOTALL)

if all([experience_match, toolkit_match, awards_match, leadership_match, testimonials_match]):
    # Remove from current locations
    content = content.replace(toolkit_match.group(1), '')
    content = content.replace(awards_match.group(1), '')
    content = content.replace(testimonials_match.group(1), '')

    # Insert Toolkit and Awards after Experience
    # Actually, we will just place them immediately after EXPERIENCE END so they flow right after Experience.
    content = content.replace(
        '<!-- EXPERIENCE END -->',
        '<!-- EXPERIENCE END -->\n\n' + toolkit_match.group(1) + '\n\n' + awards_match.group(1)
    )

    # Insert Testimonials after Leadership
    content = content.replace(
        '<!-- LEADERSHIP END -->',
        '<!-- LEADERSHIP END -->\n\n' + testimonials_match.group(1)
    )

with open('d:/other/princenwalozie/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reordering complete.")
