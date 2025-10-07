import reflex as rx
from app.states.state import State
from app.components.navbar import navbar
from app.components.footer import footer
from app.pages.home import home_page
from app.pages.about import about_page
from app.pages.contact import contact_page
from app.pages.sii_conn import sii_conn_page


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.match(
                State.current_page,
                ("home", home_page()),
                ("about", about_page()),
                ("contact", contact_page()),
                ("sii_conn", sii_conn_page()),
                home_page(),
            )
        ),
        footer(),
        rx.cond(
            State.show_scroll_top_button,
            rx.el.button(
                rx.icon("arrow-up"),
                on_click=rx.call_script(
                    "window.scrollTo({top: 0, behavior: 'smooth'})"
                ),
                class_name="fixed bottom-8 right-8 bg-orange-500 text-white p-3 rounded-full shadow-lg hover:bg-orange-600 transition-all z-50 animate-fade-in",
            ),
        ),
        on_mount=rx.call_script("""
            const handleScroll = () => {
                const isScrolled = window.scrollY > 200;
                if (isScrolled !== window._isScrolled) {
                    window._isScrolled = isScrolled;
                    _reflex_internal.event_handlers.State.set_show_scroll_top_button(isScrolled);
                }
            };
            window.addEventListener('scroll', handleScroll, { passive: true });
            handleScroll();
            """),
        class_name="bg-gray-900 font-['Raleway']",
        id="main-container",
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="orange"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700;800&display=swap",
            rel="stylesheet",
        ),
        rx.el.style("""
            @keyframes marquee {
                0% { transform: translateX(0%); }
                100% { transform: translateX(-50%); }
            }
            .animate-marquee {
                animation: marquee 30s linear infinite;
            }
            @keyframes fade-in {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            .animate-fade-in {
                animation: fade-in 0.3s ease-in-out;
            }
            """),
    ],
)
app.add_page(index, title="Tech Solutions - Innovación y Desarrollo")