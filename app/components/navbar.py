import reflex as rx
from app.states.state import State


def navbar_link(text: str, page_name: str) -> rx.Component:
    return rx.el.a(
        text,
        on_click=State.set_page(page_name),
        class_name=rx.cond(
            State.current_page == page_name,
            "px-4 py-2 text-orange-500 font-semibold border-b-2 border-orange-500 cursor-pointer",
            "px-4 py-2 text-white hover:text-orange-400 transition-colors duration-300 cursor-pointer",
        ),
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src="/modern_technology_company.png", class_name="h-20 w-auto"
                ),
                rx.el.div(
                    rx.el.h1(
                        "Tech Solutions",
                        class_name="text-2xl font-bold text-white tracking-wider",
                    ),
                    rx.el.p(
                        "Innovación y Desarrollo Tecnológico",
                        class_name="text-sm text-gray-300",
                    ),
                    class_name="ml-4",
                ),
                class_name="flex items-center",
            ),
            rx.el.nav(
                navbar_link("Inicio", "home"),
                navbar_link("Sobre Nosotros", "about"),
                navbar_link("Contacto", "contact"),
                class_name="hidden md:flex items-center space-x-4",
            ),
            class_name="container mx-auto px-6 py-6 flex justify-between items-center",
        ),
        class_name="bg-gray-900/80 backdrop-blur-md sticky top-0 z-50 shadow-lg border-b border-blue-800/30",
    )