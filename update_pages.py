import re

# 1. Update about.html
about_file = 'd:/other/princenwalozie/about.html'
with open(about_file, 'r', encoding='utf-8') as f:
    about_content = f.read()

new_bio = """
                <h2 class="font-heading text-2xl font-bold text-gray-900 dark:text-white mb-4">Biography</h2>
                <p class="text-gray-700 dark:text-gray-300 leading-relaxed text-lg">
                    Dynamic and results-driven student at Stanford University with a strong foundation in Management Science and Engineering. Passionate about bridging the gap between technical engineering and strategic product management. Experienced in data analytics, Python, and cross-functional leadership, with a proven track record of delivering user-centric solutions. Always eager to explore the intersections of AI, finance, and equitable tech.
                </p>
"""

# Replace the bio content
about_content = re.sub(
    r'<h2 class="font-heading text-2xl font-bold text-gray-900 dark:text-white mb-4">Biography</h2>.*?</p>',
    new_bio.strip(),
    about_content,
    flags=re.DOTALL
)

# Rename "Technical Skills" to "Skills" if user just wanted it called "Skills"
about_content = about_content.replace('Technical Skills', 'Skills')

with open(about_file, 'w', encoding='utf-8') as f:
    f.write(about_content)


# 2. Update script.js for click-through albums
script_file = 'd:/other/princenwalozie/script.js'
with open(script_file, 'r', encoding='utf-8') as f:
    script_content = f.read()

click_album_js = """
    // 6. Click-through Image Album
    const albums = document.querySelectorAll('.click-album');
    albums.forEach(album => {
        const images = album.querySelectorAll('img');
        if (images.length > 1) {
            let activeIndex = 0;
            
            // Set initial state
            images.forEach((img, index) => {
                img.style.position = 'absolute';
                img.style.top = '0';
                img.style.left = '0';
                img.style.width = '100%';
                img.style.height = '100%';
                img.style.transition = 'opacity 0.4s ease-in-out, transform 0.4s ease-in-out';
                
                if (index === 0) {
                    img.style.opacity = '1';
                    img.style.transform = 'scale(1) rotate(0deg)';
                    img.style.zIndex = '10';
                } else {
                    img.style.opacity = '0';
                    img.style.transform = `scale(0.95) rotate(${(Math.random() - 0.5) * 6}deg)`;
                    img.style.zIndex = '0';
                }
            });

            // On click
            album.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Animate out current
                images[activeIndex].style.opacity = '0';
                images[activeIndex].style.transform = `scale(0.95) rotate(${(Math.random() - 0.5) * 6}deg)`;
                images[activeIndex].style.zIndex = '0';
                
                // Increment index
                activeIndex = (activeIndex + 1) % images.length;
                
                // Animate in next
                images[activeIndex].style.opacity = '1';
                images[activeIndex].style.transform = 'scale(1) rotate(0deg)';
                images[activeIndex].style.zIndex = '10';
            });
        }
    });
"""

if '// 6. Click-through Image Album' not in script_content:
    # Insert before the last });
    script_content = script_content.replace('});\n', click_album_js + '});\n')
    
    with open(script_file, 'w', encoding='utf-8') as f:
        f.write(script_content)


# 3. Update blog-list.html to use the click-album class instead of hover slider
blog_file = 'd:/other/princenwalozie/blog-list.html'
with open(blog_file, 'r', encoding='utf-8') as f:
    blog_content = f.read()

# Replace the specific inner album structure
old_album = """<div class="absolute inset-0 flex transition-transform duration-700 ease-in-out group-hover/album:-translate-x-full">
                        <img src="assets/blog_cluster_1_1781859651533.png" alt="AI and Finance" class="w-full h-full object-cover flex-shrink-0">
                        <img src="assets/blog_cluster_2_1781859665993.png" alt="Product Strategy" class="w-full h-full object-cover flex-shrink-0">
                    </div>
                    <div class="absolute bottom-4 right-4 bg-black/60 text-white text-xs px-3 py-1.5 rounded-none backdrop-blur font-semibold tracking-wide flex items-center gap-2">
                        <i class="fas fa-images"></i> Hover to explore
                    </div>"""

new_album = """<div class="absolute inset-0 click-album w-full h-full">
                        <img src="assets/blog_cluster_1_1781859651533.png" alt="AI and Finance" class="w-full h-full object-cover shadow-[4px_4px_0px_#10B981]">
                        <img src="assets/blog_cluster_2_1781859665993.png" alt="Product Strategy" class="w-full h-full object-cover shadow-[4px_4px_0px_#3B82F6]">
                    </div>
                    <div class="absolute bottom-4 right-4 bg-black/80 text-white text-xs px-3 py-1.5 rounded-none backdrop-blur font-semibold tracking-wide flex items-center gap-2 z-20 pointer-events-none">
                        <i class="fas fa-hand-pointer"></i> Click to explore
                    </div>"""

blog_content = blog_content.replace(old_album, new_album)
blog_content = blog_content.replace('group-hover/album cursor-pointer', 'cursor-pointer')

with open(blog_file, 'w', encoding='utf-8') as f:
    f.write(blog_content)

print("Page-specific changes applied.")
