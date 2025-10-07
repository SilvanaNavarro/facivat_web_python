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
        class_name="bg-gray-900 font-['Raleway']",
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
            """),
    ],
)
app.add_page(index, title="Tech Solutions - Innovación y Desarrollo")