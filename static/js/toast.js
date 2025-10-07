function showToast(message, type = 'info', duration = 5000) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    // Add the base class for transitions
    toast.className = 'toast-item glassmorphism'; // Use the glassmorphism effect

    // Set styles based on type to match the website theme
    const styles = {
        success: {
            border: 'border-brand-accent-lime', // Lime green accent border
            icon: '✅'
        },
        error: {
            border: 'border-red-500',         // Red accent border
            icon: '❌'
        },
        info: {
            border: 'border-blue-500',          // Blue accent border
            icon: 'ℹ️'
        }
    };
    
    const style = styles[type] || styles.info;
    
    toast.classList.add(
        style.border, 
        'p-4', 'rounded-lg', 'shadow-2xl', 'flex', 'items-start', 
        'gap-4', 'border-l-4', 'transform', 'translate-x-full', 
        'opacity-0', 'text-brand-light-gray' // Use light text for dark background
    );

    toast.innerHTML = `
        <span class="text-xl pt-1">${style.icon}</span>
        <div class="flex-grow">
            <p class="font-bold font-orbitron">${type.charAt(0).toUpperCase() + type.slice(1)}</p>
            <p class="text-sm">${message}</p>
        </div>
        <button class="ml-auto text-2xl text-gray-500 hover:text-white transition-colors">&times;</button>
    `;

    container.appendChild(toast);

    // Animate in
    setTimeout(() => {
        toast.classList.remove('translate-x-full', 'opacity-0');
    }, 50);

    // Function to remove the toast
    const removeToast = () => {
        toast.classList.add('opacity-0');
        // Slide out to the right instead of just fading
        toast.classList.add('translate-x-4'); 
        toast.addEventListener('transitionend', () => {
            toast.remove();
        });
    };

    const timer = setTimeout(removeToast, duration);

    toast.querySelector('button').addEventListener('click', () => {
        clearTimeout(timer);
        removeToast();
    });
}