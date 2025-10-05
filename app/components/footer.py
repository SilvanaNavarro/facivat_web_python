import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "© 2025 FACIVAT SpA. Todos los derechos reservados.",
                    class_name="text-sm text-gray-400",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            "twitter",
                            class_name="h-6 w-6 text-gray-400 hover:text-orange-500 transition",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "linkedin",
                            class_name="h-6 w-6 text-gray-400 hover:text-orange-500 transition",
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "github",
                            class_name="h-6 w-6 text-gray-400 hover:text-orange-500 transition",
                        ),
                        href="#",
                    ),
                    class_name="flex space-x-4",
                ),
                class_name="container mx-auto px-6 py-4 flex justify-between items-center",
            ),
            class_name="border-t border-gray-800",
        ),
        class_name="bg-gray-900 text-white",
    )