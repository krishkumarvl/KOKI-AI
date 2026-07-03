document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const track = document.querySelector('.tour-slides-track');
    const slides = Array.from(document.querySelectorAll('.tour-slide'));
    const dots = Array.from(document.querySelectorAll('.tour-dot'));
    const prevBtn = document.querySelector('.tour-nav-btn.prev');
    const nextBtn = document.querySelector('.tour-nav-btn.next');
    const slider = document.querySelector('.tour-slider');

    if (!track || slides.length === 0) return;

    let currentIndex = 0;
    const totalSlides = slides.length;

    // Go to slide
    function goToSlide(index) {
        // Enforce boundary wrapping
        if (index < 0) {
            currentIndex = totalSlides - 1;
        } else if (index >= totalSlides) {
            currentIndex = 0;
        } else {
            currentIndex = index;
        }

        // Translate the track
        track.style.transform = `translateX(-${currentIndex * 100}%)`;

        // Update active class on slides
        slides.forEach((slide, i) => {
            if (i === currentIndex) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });

        // Update active dot and aria-selected states
        dots.forEach((dot, i) => {
            if (i === currentIndex) {
                dot.classList.add('active');
                dot.setAttribute('aria-selected', 'true');
            } else {
                dot.classList.remove('active');
                dot.setAttribute('aria-selected', 'false');
            }
        });
    }

    // Next / Prev slide handlers
    function nextSlide() {
        goToSlide(currentIndex + 1);
    }

    function prevSlide() {
        goToSlide(currentIndex - 1);
    }

    // Button click events
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);

    // Dot click events
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            goToSlide(index);
        });
    });

    // Keyboard arrow keys navigation (when slider is visible)
    window.addEventListener('keydown', (e) => {
        if (!slider) return;
        
        // Check if slider is in viewport
        const rect = slider.getBoundingClientRect();
        const inViewport = rect.top < window.innerHeight && rect.bottom > 0;
        
        if (inViewport) {
            if (e.key === 'ArrowRight') {
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                prevSlide();
            }
        }
    });

    // Touch Swipe Support for Mobile
    let startX = 0;
    let endX = 0;
    
    if (slider) {
        slider.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
        }, { passive: true });

        slider.addEventListener('touchend', (e) => {
            endX = e.changedTouches[0].clientX;
            handleSwipe();
        }, { passive: true });
    }

    function handleSwipe() {
        const swipeThreshold = 50; // Minimum drag distance in pixels
        const diff = startX - endX;

        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                // Swiped left -> show next slide
                nextSlide();
            } else {
                // Swiped right -> show previous slide
                prevSlide();
            }
        }
    }

    // ==========================================
    // INTERACTIVE WEEKLY TIMELINE
    // ==========================================
    const weekData = {
        1: {
            version: "Week 1 &bull; Alpha v0.1",
            progress: "10%",
            completed: [
                "&#9989; Conversational Prototype",
                "&#9989; Personality Definition",
                "&#9989; Basic Input/Output Handler"
            ],
            building: "Memory Architecture",
            next: "Persistent Context Storage",
            northStar: "KORAIN",
            lesson: "Starting is the hardest part. Stop overthinking and write the first line of code."
        },
        2: {
            version: "Week 2 &bull; Alpha v0.2",
            progress: "22%",
            completed: [
                "&#9989; Local JSON Database",
                "&#9989; Evolving Context Logic",
                "&#9989; Simple Multi-turn Conversations"
            ],
            building: "Modular Architecture",
            next: "Integrated UI Dashboard",
            northStar: "KORAIN",
            lesson: "AI memory isn't just about saving text—it is about retrieval and context relevance."
        },
        3: {
            version: "Week 3 &bull; Alpha v0.3",
            progress: "30%",
            completed: [
                "&#9989; Interface Mockups",
                "&#9989; Responsive Colors & Palette",
                "&#9989; Setup Layout Setup"
            ],
            building: "Tool calling layer",
            next: "Community and Feedback Hub",
            northStar: "KORAIN",
            lesson: "A great product deserves a calm interface. Visual noise is a distraction."
        },
        4: {
            version: "Week 4 &bull; Alpha v1",
            progress: "38%",
            completed: [
                "&#9989; Landing Website",
                "&#9989; Product Showcase",
                "&#9989; Memory Architecture",
                "&#9989; Community & Feedback"
            ],
            building: "Tool Layer Integration",
            next: "Voice Assistant",
            northStar: "KORAIN",
            lesson: "Build first, perfect later &mdash; shipping teaches more than planning ever does."
        }
    };

    const statusTabs = document.querySelectorAll('.status-tab');
    const statusContent = document.getElementById('status-content');
    const weekBadge = document.getElementById('status-week-badge');
    const progressText = document.getElementById('status-progress-text');
    const progressFill = document.getElementById('status-progress-fill');
    const completedList = document.getElementById('status-completed-list');
    const buildingText = document.getElementById('status-building-text');
    const milestoneText = document.getElementById('status-milestone-text');
    const northstarText = document.getElementById('status-northstar-text');
    const lessonText = document.getElementById('status-lesson-text');

    if (statusTabs.length > 0 && statusContent) {
        statusTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const week = tab.getAttribute('data-week');
                const data = weekData[week];

                if (!data) return;

                // 1. Remove active class from all tabs
                statusTabs.forEach(t => {
                    t.classList.remove('active');
                    t.setAttribute('aria-selected', 'false');
                });

                // 2. Add active class to clicked tab
                tab.classList.add('active');
                tab.setAttribute('aria-selected', 'true');

                // 3. Fade out detail wrapper
                statusContent.classList.add('fade-out');

                // 4. Update elements after fade out completes
                setTimeout(() => {
                    weekBadge.innerHTML = data.version;
                    progressText.textContent = data.progress;
                    progressFill.style.width = data.progress;

                    // Rebuild completed list
                    completedList.innerHTML = data.completed.map(item => `<li>${item}</li>`).join('');

                    buildingText.textContent = data.building;
                    milestoneText.textContent = data.next;
                    northstarText.textContent = data.northStar;
                    lessonText.innerHTML = data.lesson;

                    // 5. Fade back in
                    statusContent.classList.remove('fade-out');
                }, 350); // matches CSS transition time (.35s)
            });
        });
    }

    // ==========================================
    // INTERACTIVE TECH ECOSYSTEM
    // ==========================================
    const techData = {
        python: {
            title: "Python",
            url: "https://www.python.org",
            purpose: "Powers KOKI's backend reasoning, file operations, local database memory indexing, and automation scripts.",
            chosen: "Industry-standard library ecosystem for AI integrations, clean syntax, and fast prototyping speed.",
            contrib: "Acts as the core execution engine of the OS, driving conversational loops and managing system tool integrations.",
            usage: "Active backend controller handling FastAPI endpoints, JSON database reads/writes, and background worker threads."
        },
        html5: {
            title: "HTML5",
            url: "https://developer.mozilla.org/en-US/docs/Web/HTML",
            purpose: "Semantic markup structure of KOKI's user interface and landing pages.",
            chosen: "Standard, lightweight foundation of modern browsers with native accessibility support.",
            contrib: "Provides clear document structures, interactive elements, and accessible tab hierarchies.",
            usage: "Structures the landing portfolio layout, timeline panels, and product carousels."
        },
        css3: {
            title: "CSS3",
            url: "https://developer.mozilla.org/en-US/docs/Web/CSS",
            purpose: "Visual style system, responsive grid layouts, animations, and micro-interactions.",
            chosen: "Maximum speed, styling control, and zero overhead compared to bulky frameworks.",
            contrib: "Preserves the warm 'Digital Atelier' parchment aesthetics, custom hover animations, and dark modes.",
            usage: "Handles all variables, font styling, Apple-inspired transitions, and mobile viewport optimizations."
        },
        javascript: {
            title: "JavaScript",
            url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
            purpose: "Client-side interactivity, slider controls, tab swaps, and scroll reveals.",
            chosen: "Native web standard, enabling smooth client transitions without the overhead of heavy frameworks.",
            contrib: "Links structural layout nodes to dynamic click listeners and touch sweep gestures.",
            usage: "Controls the Product Tour transitions, Weekly timeline shifts, and responsive drawer toggles."
        },
        gemini: {
            title: "Google Gemini",
            url: "https://deepmind.google/technologies/gemini/",
            purpose: "The primary LLM brain driving reasoning and conversation.",
            chosen: "Excellent multi-turn reasoning capabilities, advanced tool-calling accuracy, and native support.",
            contrib: "Acts as the conversational interpreter, decoding Hinglish dialogue and system instructions.",
            usage: "Powers KOKI's brain module reasoning, multi-turn dialogue memory, and planning layers."
        },
        stitch: {
            title: "Google Stitch",
            url: "https://stitch.google",
            purpose: "Rapid visual UI generation and canvas exploration.",
            chosen: "Generates clean layouts directly from descriptions, allowing rapid experimentation of visual styles.",
            contrib: "Helped explore and refine early ideas for the 'Digital Atelier' layout before writing code.",
            usage: "Used for exploratory wireframing and prototyping layouts during the sprint design phase."
        },
        claude: {
            title: "Claude",
            url: "https://www.anthropic.com/claude",
            purpose: "AI frontend pair-programming assistant.",
            chosen: "Exceptional understanding of code context, clean component design advice, and CSS formatting skills.",
            contrib: "Helped refactor CSS stylesheet rules, optimize grids, and verify DOM layouts.",
            usage: "Active dialogue helper for structural layout implementation and front-end optimization."
        },
        chatgpt: {
            title: "ChatGPT",
            url: "https://openai.com/chatgpt",
            purpose: "Product thinking, roadmap scheduling, and architectural strategy.",
            chosen: "Strong brainstorming capability, structured project planning, and documentation support.",
            contrib: "Helped brainstorm core memory architecture and write the 'Behind the Build' collaborative narrative.",
            usage: "Active partner for design reviews, documentation, and product planning."
        },
        antigravity: {
            title: "Antigravity IDE",
            url: "https://deepmind.google",
            purpose: "The unified agentic coding workspace.",
            chosen: "Provides native agent-assist integration, custom workspace context, and file automation features.",
            contrib: "Hosts the current implementation sandbox, allowing seamless edits and visual validation.",
            usage: "The active development workspace serving file modifications and browser checks."
        },
        github: {
            title: "GitHub",
            url: "https://github.com",
            purpose: "Version control database and open-source public commit logs.",
            chosen: "Industry-standard platform for hosting repository code and tracking development history.",
            contrib: "Powers the 'Building in Public' mission, hosting KOKI OS's open codebase and issues tracker.",
            usage: "Main repository host for KOKI AI, documenting each sprint's commits."
        },
        vscode: {
            title: "VS Code",
            url: "https://code.visualstudio.com",
            purpose: "Primary offline code editing software.",
            chosen: "Extensible interface, fast operations, and integrated terminal support.",
            contrib: "The physical desktop workspace where Krish translates mockups into codebase files.",
            usage: "Active editor for backend API development and script writing."
        },
        vercel: {
            title: "Vercel",
            url: "https://vercel.com",
            purpose: "Production hosting platform for the landing page.",
            chosen: "Blazing-fast global CDN edge, simple Git deployments, and excellent page speeds.",
            contrib: "Hosts the public URL, serving the landing page with optimal visual delivery and fast initial loading.",
            usage: "Automated hosting target linked directly to GitHub commits."
        },
        jotform: {
            title: "Jotform",
            url: "https://www.jotform.com",
            purpose: "Interactive feedback forms.",
            chosen: "Secure, customizable input forms requiring zero database configuration.",
            contrib: "Provides the bridge for visitor feedback, bug reporting, and feature suggestion collections.",
            usage: "Linked directly to the CTA button under the feedback section."
        }
    };

    const techButtons = document.querySelectorAll('.tech-logo-btn');
    const techCard = document.getElementById('tech-detail-panel');
    const techTitle = document.getElementById('tech-detail-title');
    const techLink = document.getElementById('tech-detail-link');
    const techPurpose = document.getElementById('tech-detail-purpose');
    const techChosen = document.getElementById('tech-detail-chosen');
    const techContrib = document.getElementById('tech-detail-contrib');
    const techUsage = document.getElementById('tech-detail-usage');

    if (techButtons.length > 0 && techCard) {
        techButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const techKey = btn.getAttribute('data-tech');
                const data = techData[techKey];

                if (!data) return;

                // 1. Remove active state from other buttons
                techButtons.forEach(b => {
                    b.classList.remove('active');
                    b.setAttribute('aria-selected', 'false');
                });

                // 2. Set current button active
                btn.classList.add('active');
                btn.setAttribute('aria-selected', 'true');

                // 3. Smooth fade transition
                techCard.classList.add('fade-out');

                setTimeout(() => {
                    // Update details
                    techTitle.textContent = data.title;
                    techLink.setAttribute('href', data.url);
                    techPurpose.textContent = data.purpose;
                    techChosen.textContent = data.chosen;
                    techContrib.textContent = data.contrib;
                    techUsage.textContent = data.usage;

                    // Fade back in
                    techCard.classList.remove('fade-out');
                }, 350);
            });
        });
    }
});
