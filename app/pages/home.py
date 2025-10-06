import reflex as rx
from app.states.state import State


def animated_service_banner() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                State.services,
                lambda service: rx.el.div(
                    rx.el.img(src=service.image, class_name="h-48 w-full object-cover"),
                    rx.el.p(
                        service.description,
                        class_name="mt-2 text-center font-semibold text-white",
                    ),
                    class_name="flex-none w-64 mx-4 p-4 bg-gray-800/50 rounded-lg shadow-xl",
                ),
            ),
            rx.foreach(
                State.services,
                lambda service: rx.el.div(
                    rx.el.img(src=service.image, class_name="h-48 w-full object-cover"),
                    rx.el.p(
                        service.description,
                        class_name="mt-2 text-center font-semibold text-white",
                    ),
                    class_name="flex-none w-64 mx-4 p-4 bg-gray-800/50 rounded-lg shadow-xl",
                ),
            ),
            class_name="flex animate-marquee",
        ),
        class_name="relative w-full overflow-hidden bg-gradient-to-r from-blue-900 to-gray-900 py-8",
        custom_attrs={
            "style": {
                "mask-image": "linear-gradient(to right, transparent, black 20%, black 80%, transparent)"
            }
        },
    )


def sii_connector_promo() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Presentamos ",
                    rx.el.span("SII Connector", class_name="text-orange-500"),
                    class_name="text-3xl md:text-4xl font-bold text-white mb-4",
                ),
                rx.el.p(
                    "La solución definitiva para la facturación electrónica en Chile. Integra tus sistemas directamente con el Servicio de Impuestos Internos (SII) de forma fácil, rápida y segura.",
                    class_name="text-lg text-gray-300 mb-8 max-w-2xl",
                ),
                rx.el.button(
                    "Conoce más",
                    rx.icon("arrow-right", class_name="ml-2"),
                    on_click=lambda: State.set_page("sii_conn"),
                    class_name="bg-orange-500 text-white font-bold py-3 px-8 rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-lg hover:shadow-orange-500/30 transform hover:-translate-y-1",
                ),
                class_name="md:w-1/2",
            ),
            rx.el.div(
                rx.el.video(
                    src="/sii_conn/sii_conn_promo.mp4",
                    auto_play=True,
                    loop=True,
                    muted=True,
                    plays_inline=True,
                    class_name="rounded-xl shadow-2xl w-full h-auto object-cover border-4 border-blue-800",
                ),
                class_name="md:w-1/2 mt-8 md:mt-0",
            ),
            class_name="container mx-auto px-6 py-20 flex flex-col md:flex-row items-center gap-12",
        ),
        class_name="bg-blue-900/70",
    )


def service_card(service: rx.Var[dict], index: int) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src=service["image"], class_name="w-full h-48 object-cover rounded-t-lg"
        ),
        rx.el.div(
            rx.el.h3(service["title"], class_name="text-xl font-bold text-white mb-2"),
            rx.cond(
                State.active_service_index == index,
                rx.el.button(
                    "Contactar",
                    on_click=lambda: State.set_page("contact"),
                    class_name="mt-4 w-full bg-orange-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-orange-600 transition-all",
                ),
                rx.el.p(service["description"], class_name="text-gray-400"),
            ),
            class_name="p-6",
        ),
        on_click=lambda: State.set_active_service_index(index),
        class_name="bg-gray-800/50 rounded-lg shadow-lg overflow-hidden border border-blue-800/50 transform hover:-translate-y-2 transition-transform duration-300 cursor-pointer",
    )


def other_services() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Explora Nuestros Servicios",
                class_name="text-3xl md:text-4xl font-bold text-white mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(State.other_services_list, service_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="container mx-auto px-6 py-20",
        ),
        class_name="bg-gray-900",
    )


def intro_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src="servicios.jpg",
                    class_name="rounded-xl shadow-2xl w-full h-auto object-cover",
                ),
                class_name="md:w-5/12",
            ),
            rx.el.div(
                rx.el.h2(
                    "Arquitectos de su Transformación Digital",
                    class_name="text-3xl md:text-4xl font-bold text-white mb-6",
                ),
                rx.el.p(
                    "En FACIVAT, forjamos el futuro de su empresa a través de un ecosistema de soluciones tecnológicas integrales. Desde el desarrollo de aplicaciones a medida que se adaptan a sus procesos, hasta la creación de agentes de IA de vanguardia para automatizar tareas complejas. Construimos robustas arquitecturas en la nube que garantizan escalabilidad, seguridad y acceso ininterrumpido a sus datos, sentando las bases para un crecimiento sostenible.",
                    class_name="text-gray-300 mb-4 leading-relaxed",
                ),
                rx.el.p(
                    "Ofrecemos asesoría y consultoría estratégica, guiados por Project Managers certificados, para asegurar que cada iniciativa genere un impacto medible. Integramos sus sistemas, unificando flujos de trabajo para potenciar la eficiencia. Ya sea que necesite una página web cautivadora o una consultoría experta para navegar el panorama tecnológico, somos su socio de confianza en el camino hacia la innovación.",
                    class_name="text-gray-300 leading-relaxed",
                ),
                class_name="md:w-7/12",
            ),
            class_name="container mx-auto px-6 py-20 flex flex-col-reverse md:flex-row items-center gap-12",
        ),
        class_name="bg-gray-900",
    )


def home_page() -> rx.Component:
    return rx.el.div(
        intro_section(),
        animated_service_banner(),
        sii_connector_promo(),
        other_services(),
    )