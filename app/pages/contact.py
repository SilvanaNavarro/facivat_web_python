import reflex as rx
from app.states.state import State


def contact_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Hablemos de tu Proyecto",
                    class_name="text-4xl md:text-5xl font-extrabold text-white mb-4",
                ),
                rx.el.p(
                    "Estamos aquí para ayudarte a llevar tus ideas al siguiente nivel. Completa el formulario y nos pondremos en contacto contigo.",
                    class_name="text-lg text-gray-300 max-w-lg",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("map-pin", class_name="h-6 w-6 text-orange-500 mr-3"),
                        "Santiago, Chile",
                        class_name="flex items-center text-gray-300 mt-8",
                    ),
                    rx.el.div(
                        rx.icon("mail", class_name="h-6 w-6 text-orange-500 mr-3"),
                        "contacto@techsolutions.cl",
                        class_name="flex items-center text-gray-300 mt-4",
                    ),
                    rx.el.div(
                        rx.icon("phone", class_name="h-6 w-6 text-orange-500 mr-3"),
                        "+56 9 1234 5678",
                        class_name="flex items-center text-gray-300 mt-4",
                    ),
                ),
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.h2(
                        "Envíanos un Mensaje",
                        class_name="text-2xl font-bold text-white mb-6",
                    ),
                    rx.el.input(
                        name="name",
                        placeholder="Nombre Completo",
                        required=True,
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-4",
                    ),
                    rx.el.input(
                        name="email",
                        type="email",
                        placeholder="Correo Electrónico",
                        required=True,
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-4",
                    ),
                    rx.el.input(
                        name="subject",
                        placeholder="Asunto",
                        required=True,
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-4",
                    ),
                    rx.el.textarea(
                        name="message",
                        placeholder="Tu mensaje...",
                        required=True,
                        rows="5",
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-6",
                    ),
                    rx.el.button(
                        "Enviar Mensaje",
                        type="submit",
                        class_name="w-full bg-orange-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-lg hover:shadow-orange-500/40 transform hover:-translate-y-1",
                    ),
                    on_submit=State.handle_submit,
                    reset_on_submit=False,
                    id="contact-form",
                    class_name="w-full",
                ),
                class_name="bg-gray-900/50 p-8 rounded-xl shadow-2xl border border-blue-800/50",
            ),
            class_name="container mx-auto px-6 py-20 grid md:grid-cols-2 gap-16 items-center",
        ),
        class_name="bg-blue-900",
    )