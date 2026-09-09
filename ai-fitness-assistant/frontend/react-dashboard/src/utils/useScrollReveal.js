import { useEffect, useRef } from "react";

/**
 * useScrollReveal
 * Attaches an IntersectionObserver to the returned ref.
 * When the element enters the viewport, the 'revealed' class is added.
 *
 * @param {object} options
 * @param {number} options.threshold  - 0-1, how much of the element must be visible (default 0.12)
 * @param {number} options.delay      - extra CSS delay in ms applied via inline style (default 0)
 * @param {string} options.direction  - 'up' | 'left' | 'right' | 'scale' (default 'up')
 * @param {boolean} options.once     - only animate once (default true)
 */
export function useScrollReveal({
    threshold = 0.12,
    delay = 0,
    direction = "up",
    once = true,
} = {}) {
    const ref = useRef(null);

    useEffect(() => {
        const el = ref.current;
        if (!el) return;

        // Apply the initial hidden class based on direction
        el.classList.add(`sr-init`, `sr-${direction}`);
        if (delay) el.style.transitionDelay = `${delay}ms`;

        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting) {
                    el.classList.add("sr-revealed");
                    if (once) observer.unobserve(el);
                } else if (!once) {
                    el.classList.remove("sr-revealed");
                }
            },
            { threshold }
        );

        observer.observe(el);
        return () => observer.disconnect();
    }, [threshold, delay, direction, once]);

    return ref;
}

/**
 * ScrollReveal wrapper component for inline use
 */
export function Reveal({ children, delay = 0, direction = "up", threshold = 0.12, style = {}, className = "" }) {
    const ref = useScrollReveal({ delay, direction, threshold });
    return (
        <div ref={ref} className={className} style={style}>
            {children}
        </div>
    );
}
