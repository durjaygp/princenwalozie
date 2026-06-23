import re

blog_file = 'd:/other/princenwalozie/blog-list.html'

with open(blog_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_magazine_layout = """
    <section class="py-12 md:py-20 flex-grow">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 reveal">
            
            <!-- Featured Hero Article -->
            <article class="flex flex-col lg:flex-row bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 shadow-[8px_8px_0px_#111827] dark:shadow-[8px_8px_0px_#10B981] group hover:-translate-y-1 hover:-translate-x-1 hover:shadow-[12px_12px_0px_#111827] dark:hover:shadow-[12px_12px_0px_#10B981] transition-all duration-300 relative overflow-hidden z-10">
                <div class="lg:w-3/5 overflow-hidden border-b-2 lg:border-b-0 lg:border-r-2 border-gray-900 dark:border-gray-700 relative h-80 lg:h-auto">
                    <!-- Unsplash: Finance/Abstract -->
                    <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=1200&auto=format&fit=crop" alt="Featured Article" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute top-4 left-4 bg-primary text-white font-bold px-4 py-1.5 uppercase tracking-wider text-sm border-2 border-gray-900 shadow-[4px_4px_0px_#111827]">Cover Story</div>
                </div>
                <div class="lg:w-2/5 p-8 md:p-12 lg:p-16 flex flex-col justify-center bg-white dark:bg-gray-800 relative z-20">
                    <div class="flex items-center gap-4 mb-6">
                        <span class="text-xs font-bold text-primary uppercase tracking-widest border border-primary px-2 py-1">AI x Finance</span>
                        <span class="text-gray-500 text-xs font-semibold uppercase tracking-wider">June 20, 2026</span>
                    </div>
                    <a href="blog-details.html">
                        <h2 class="font-heading text-4xl md:text-5xl font-extrabold text-gray-900 dark:text-white mb-6 group-hover:text-primary transition-colors leading-[1.1] tracking-tight">The Intersection of Markets & Machine Learning</h2>
                    </a>
                    <p class="text-gray-600 dark:text-gray-400 text-lg md:text-xl leading-relaxed mb-10 flex-grow">
                        Diving deep into how predictive modeling and algorithmic strategies are shaping the future of global markets. Exploring the implications of real-time data analysis and its ethical considerations in automated trading systems.
                    </p>
                    <div>
                        <a href="blog-details.html" class="inline-flex items-center justify-center bg-gray-900 dark:bg-white text-white dark:text-gray-900 border-2 border-gray-900 dark:border-white hover:bg-primary hover:text-white hover:border-primary dark:hover:bg-primary dark:hover:border-primary font-bold py-3.5 px-8 transition-colors text-sm uppercase tracking-widest w-full sm:w-auto">
                            Read Article <i class="fas fa-arrow-right ml-3"></i>
                        </a>
                    </div>
                </div>
            </article>

            <!-- Editorial Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10 mt-16 md:mt-24">
                
                <!-- Article 1 -->
                <article class="flex flex-col bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 shadow-[4px_4px_0px_#111827] dark:shadow-[4px_4px_0px_#10B981] group hover:-translate-y-1 hover:-translate-x-1 hover:shadow-[8px_8px_0px_#111827] dark:hover:shadow-[8px_8px_0px_#10B981] transition-all duration-300 h-full">
                    <div class="h-56 overflow-hidden border-b-2 border-gray-900 dark:border-gray-700 relative">
                        <!-- Unsplash: AI/Tech -->
                        <img src="https://images.unsplash.com/photo-1620712948343-003a60d22c82?q=80&w=800&auto=format&fit=crop" alt="AI in Education" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <div class="p-6 md:p-8 flex flex-col flex-grow">
                        <div class="flex items-center justify-between mb-4">
                            <span class="text-xs font-bold text-secondary uppercase tracking-widest">Education Tech</span>
                            <span class="text-gray-500 text-xs font-semibold uppercase">Jun 12</span>
                        </div>
                        <a href="blog-details.html" class="flex-grow">
                            <h3 class="font-heading text-2xl md:text-3xl font-extrabold text-gray-900 dark:text-white mb-4 group-hover:text-secondary transition-colors leading-tight tracking-tight">The Future of AI in Education</h3>
                            <p class="text-gray-600 dark:text-gray-400 text-base leading-relaxed mb-8">
                                How predictive modeling and machine learning can be leveraged to customize learning experiences, alongside the challenges of data privacy.
                            </p>
                        </a>
                        <div class="mt-auto pt-4 border-t-2 border-gray-100 dark:border-gray-700">
                            <a href="blog-details.html" class="inline-flex items-center text-gray-900 dark:text-white font-extrabold hover:text-secondary dark:hover:text-secondary transition-colors uppercase text-xs tracking-widest w-full justify-between">
                                Read More <i class="fas fa-long-arrow-alt-right"></i>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- Article 2 -->
                <article class="flex flex-col bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 shadow-[4px_4px_0px_#111827] dark:shadow-[4px_4px_0px_#10B981] group hover:-translate-y-1 hover:-translate-x-1 hover:shadow-[8px_8px_0px_#111827] dark:hover:shadow-[8px_8px_0px_#10B981] transition-all duration-300 h-full">
                    <div class="h-56 overflow-hidden border-b-2 border-gray-900 dark:border-gray-700 relative">
                        <!-- Unsplash: Strategy/Startup -->
                        <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop" alt="Product Strategy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <div class="p-6 md:p-8 flex flex-col flex-grow">
                        <div class="flex items-center justify-between mb-4">
                            <span class="text-xs font-bold text-purple-600 dark:text-purple-400 uppercase tracking-widest">Product Strategy</span>
                            <span class="text-gray-500 text-xs font-semibold uppercase">May 28</span>
                        </div>
                        <a href="blog-details.html" class="flex-grow">
                            <h3 class="font-heading text-2xl md:text-3xl font-extrabold text-gray-900 dark:text-white mb-4 group-hover:text-purple-600 dark:hover:text-purple-400 transition-colors leading-tight tracking-tight">Optimizing Cross-Functional Teams</h3>
                            <p class="text-gray-600 dark:text-gray-400 text-base leading-relaxed mb-8">
                                Strategies for aligning engineering, design, and business goals to deliver scalable and sustainable solutions in early-stage startups.
                            </p>
                        </a>
                        <div class="mt-auto pt-4 border-t-2 border-gray-100 dark:border-gray-700">
                            <a href="blog-details.html" class="inline-flex items-center text-gray-900 dark:text-white font-extrabold hover:text-purple-600 dark:hover:text-purple-400 transition-colors uppercase text-xs tracking-widest w-full justify-between">
                                Read More <i class="fas fa-long-arrow-alt-right"></i>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- Article 3 -->
                <article class="flex flex-col bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 shadow-[4px_4px_0px_#111827] dark:shadow-[4px_4px_0px_#10B981] group hover:-translate-y-1 hover:-translate-x-1 hover:shadow-[8px_8px_0px_#111827] dark:hover:shadow-[8px_8px_0px_#10B981] transition-all duration-300 h-full">
                    <div class="h-56 overflow-hidden border-b-2 border-gray-900 dark:border-gray-700 relative">
                        <!-- Unsplash: Analytics -->
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop" alt="Data Products" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <div class="p-6 md:p-8 flex flex-col flex-grow">
                        <div class="flex items-center justify-between mb-4">
                            <span class="text-xs font-bold text-pink-600 dark:text-pink-400 uppercase tracking-widest">Data Analytics</span>
                            <span class="text-gray-500 text-xs font-semibold uppercase">May 15</span>
                        </div>
                        <a href="blog-details.html" class="flex-grow">
                            <h3 class="font-heading text-2xl md:text-3xl font-extrabold text-gray-900 dark:text-white mb-4 group-hover:text-pink-600 dark:hover:text-pink-400 transition-colors leading-tight tracking-tight">Building User-Centric Data Products</h3>
                            <p class="text-gray-600 dark:text-gray-400 text-base leading-relaxed mb-8">
                                Bridging the gap between complex data pipelines and intuitive, engaging user interfaces to maximize user retention and understanding.
                            </p>
                        </a>
                        <div class="mt-auto pt-4 border-t-2 border-gray-100 dark:border-gray-700">
                            <a href="blog-details.html" class="inline-flex items-center text-gray-900 dark:text-white font-extrabold hover:text-pink-600 dark:hover:text-pink-400 transition-colors uppercase text-xs tracking-widest w-full justify-between">
                                Read More <i class="fas fa-long-arrow-alt-right"></i>
                            </a>
                        </div>
                    </div>
                </article>

            </div>

            <!-- Pagination -->
            <div class="mt-20 md:mt-28 flex justify-center items-center gap-2 md:gap-4">
                <button class="bg-gray-100 dark:bg-gray-800 border-2 border-gray-300 dark:border-gray-700 text-gray-400 dark:text-gray-500 px-4 md:px-6 py-2.5 font-bold opacity-50 cursor-not-allowed uppercase tracking-widest text-sm flex items-center">
                    <i class="fas fa-chevron-left mr-2"></i> Prev
                </button>
                
                <div class="hidden sm:flex items-center gap-2">
                    <button class="bg-primary text-white border-2 border-gray-900 dark:border-primary shadow-[4px_4px_0px_#111827] dark:shadow-[4px_4px_0px_#10B981] w-12 h-12 flex items-center justify-center font-extrabold transition-all text-lg -translate-y-0.5">1</button>
                    
                    <button class="bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 w-12 h-12 flex items-center justify-center font-extrabold transition-all hover:shadow-[4px_4px_0px_#111827] dark:hover:shadow-[4px_4px_0px_#10B981] hover:-translate-y-0.5 text-lg">2</button>
                    
                    <button class="bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 w-12 h-12 flex items-center justify-center font-extrabold transition-all hover:shadow-[4px_4px_0px_#111827] dark:hover:shadow-[4px_4px_0px_#10B981] hover:-translate-y-0.5 text-lg">3</button>
                    
                    <span class="w-8 h-12 flex items-center justify-center font-bold text-gray-500 tracking-widest">...</span>
                    
                    <button class="bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 w-12 h-12 flex items-center justify-center font-extrabold transition-all hover:shadow-[4px_4px_0px_#111827] dark:hover:shadow-[4px_4px_0px_#10B981] hover:-translate-y-0.5 text-lg">8</button>
                </div>
                
                <span class="sm:hidden text-gray-600 dark:text-gray-400 font-bold mx-2 text-sm uppercase tracking-widest">Pg 1 of 8</span>
                
                <button class="bg-white dark:bg-gray-800 border-2 border-gray-900 dark:border-gray-700 text-gray-900 dark:text-white hover:bg-primary hover:text-white hover:border-primary dark:hover:bg-primary dark:hover:border-primary hover:shadow-[4px_4px_0px_#111827] dark:hover:shadow-[4px_4px_0px_#10B981] hover:-translate-y-0.5 px-4 md:px-6 py-2.5 font-bold transition-all uppercase tracking-widest text-sm flex items-center">
                    Next <i class="fas fa-chevron-right ml-2"></i>
                </button>
            </div>

        </div>
    </section>
"""

# Extract and replace
start_comment = '<!-- BLOG LIST START -->'
end_comment = '<!-- BLOG LIST END -->'

if start_comment in content and end_comment in content:
    start_idx = content.find(start_comment)
    end_idx = content.find(end_comment) + len(end_comment)
    
    new_content = content[:start_idx] + start_comment + '\n' + new_magazine_layout + '\n    ' + end_comment + content[end_idx:]
    
    with open(blog_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Magazine layout applied successfully.")
else:
    print("Error: Could not find BLOG LIST comments.")
