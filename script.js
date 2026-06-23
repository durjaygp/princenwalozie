// script.js

// Ensure early dark mode execution to prevent flash of light mode
// This part should ideally be in the head, but we place it here and in HTML
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark');
}

document.addEventListener('DOMContentLoaded', () => {
    // 1. Dark Mode Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    // Change the icons inside the button based on previous settings
    if (document.documentElement.classList.contains('dark')) {
        if(themeToggleLightIcon) themeToggleLightIcon.classList.remove('hidden');
    } else {
        if(themeToggleDarkIcon) themeToggleDarkIcon.classList.remove('hidden');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            // toggle icons inside button
            if(themeToggleDarkIcon) themeToggleDarkIcon.classList.toggle('hidden');
            if(themeToggleLightIcon) themeToggleLightIcon.classList.toggle('hidden');

            // if set via local storage previously
            if (localStorage.getItem('color-theme')) {
                if (localStorage.getItem('color-theme') === 'light') {
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                } else {
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                }
            } else {
                if (document.documentElement.classList.contains('dark')) {
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
            }
        
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
});
    }

    // 2. Mobile Menu Toggle Logic
    const btn = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');

    if (btn && menu) {
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        
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
});
    }

    // 3. Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-md', 'dark:border-b', 'dark:border-gray-800');
            } else {
                navbar.classList.remove('shadow-md', 'dark:border-b', 'dark:border-gray-800');
            }
        
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
});
    }

    // 4. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('opacity-100', 'translate-y-0', 'translate-x-0');
                entry.target.classList.remove('opacity-0', 'translate-y-10', '-translate-x-10', 'translate-x-10');
            }
        
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
});
    };
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
    
    revealElements.forEach(el => {
        el.classList.add('transition-all', 'duration-700', 'ease-out');
        if(!el.classList.contains('reveal-left') && !el.classList.contains('reveal-right')) {
             el.classList.add('opacity-0', 'translate-y-10');
        } else if (el.classList.contains('reveal-left')) {
             el.classList.add('opacity-0', '-translate-x-10');
        } else if (el.classList.contains('reveal-right')) {
             el.classList.add('opacity-0', 'translate-x-10');
        }
        revealObserver.observe(el);
    
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
});

    // Trigger active class on elements already in viewport on load
    setTimeout(() => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight - 50) {
                el.classList.add('opacity-100', 'translate-y-0', 'translate-x-0');
                el.classList.remove('opacity-0', 'translate-y-10', '-translate-x-10', 'translate-x-10');
            }
        
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
});
    }, 100);

    // 5. Testimonial Carousel
    const slider = document.getElementById('testimonial-slider');
    const prevBtn = document.getElementById('prev-testimonial');
    const nextBtn = document.getElementById('next-testimonial');
    const indicatorsContainer = document.getElementById('testimonial-indicators');
    
    if (slider && prevBtn && nextBtn && indicatorsContainer) {
        const slides = slider.children;
        const totalSlides = slides.length;
        let currentIndex = 0;
        let autoplayInterval;

        // Create Indicators
        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('button');
            dot.classList.add('h-2', 'rounded-full', 'transition-all', 'duration-300', 'focus:outline-none');
            if (i === 0) {
                dot.classList.add('bg-white', 'w-8');
            } else {
                dot.classList.add('bg-white/40', 'w-2', 'hover:bg-white/60');
            }
            dot.addEventListener('click', () => {
                goToSlide(i);
                resetAutoplay();
            
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
});
            indicatorsContainer.appendChild(dot);
        }
        const dots = indicatorsContainer.children;

        const updateIndicators = () => {
            Array.from(dots).forEach((dot, index) => {
                if (index === currentIndex) {
                    dot.classList.remove('bg-white/40', 'w-2');
                    dot.classList.add('bg-white', 'w-8');
                } else {
                    dot.classList.remove('bg-white', 'w-8');
                    dot.classList.add('bg-white/40', 'w-2');
                }
            
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
});
        };

        const goToSlide = (index) => {
            currentIndex = index;
            slider.style.transform = `translateX(-${currentIndex * 100}%)`;
            updateIndicators();
        };

        const nextSlide = () => {
            currentIndex = (currentIndex + 1) % totalSlides;
            goToSlide(currentIndex);
        };

        const prevSlide = () => {
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            goToSlide(currentIndex);
        };

        const startAutoplay = () => {
            autoplayInterval = setInterval(nextSlide, 6000); // 6 seconds
        };

        const resetAutoplay = () => {
            clearInterval(autoplayInterval);
            startAutoplay();
        };

        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetAutoplay();
        
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
});

        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetAutoplay();
        
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
});

        startAutoplay();
    }

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
});
