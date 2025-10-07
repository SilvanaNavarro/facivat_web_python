import reflex as rx
from app.states.state import State


def feature_section(
    image_src: str, title: str, description: str, reverse: bool = False
) -> rx.Component:
    order_class = "md:flex-row-reverse" if reverse else "md:flex-row"
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=image_src,
                class_name="rounded-xl shadow-2xl w-full h-auto object-cover border-4 border-blue-800",
            ),
            class_name="md:w-1/2",
        ),
        rx.el.div(
            rx.el.h3(title, class_name="text-2xl font-bold text-orange-500 mb-4"),
            rx.el.p(description, class_name="text-gray-300 leading-relaxed"),
            class_name="md:w-1/2 p-4 flex flex-col justify-center",
        ),
        class_name=f"container mx-auto px-6 py-10 flex flex-col {order_class} items-center gap-8",
    )


def demo_form_dialog() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
            on_click=State.close_demo_form,
        ),
        rx.el.div(
            rx.el.div(
                rx.el.form(
                    rx.el.h2(
                        "Solicita una Demostración",
                        class_name="text-2xl font-bold text-white mb-6 text-center",
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
                        placeholder="Correo Electrónico de Trabajo",
                        required=True,
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-4",
                    ),
                    rx.el.input(
                        name="company",
                        placeholder="Nombre de la Empresa",
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-4",
                    ),
                    rx.el.textarea(
                        name="message",
                        placeholder="¿Algún requerimiento específico? (Opcional)",
                        rows="3",
                        class_name="w-full bg-gray-800 border border-blue-800 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-orange-500 mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancelar",
                            on_click=State.close_demo_form,
                            type="button",
                            class_name="w-full bg-gray-600 text-white font-bold py-3 px-6 rounded-lg hover:bg-gray-700 transition-all duration-300",
                        ),
                        rx.el.button(
                            "Enviar Solicitud",
                            type="submit",
                            class_name="w-full bg-orange-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-lg hover:shadow-orange-500/40",
                        ),
                        class_name="grid grid-cols-2 gap-4",
                    ),
                    on_submit=State.handle_submit,
                    reset_on_submit=False,
                    id="demo-contact-form",
                    class_name="w-full",
                ),
                class_name="bg-gray-900/80 backdrop-blur-md p-8 rounded-xl shadow-2xl border border-blue-800/50 w-full max-w-lg",
            ),
            class_name="flex z-50 m-4",
        ),
        class_name="fixed open:flex z-40 h-full w-full inset-0 items-center justify-center bg-transparent",
        open=State.show_demo_form,
    )


def sii_conn_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "SII Connector: Facturación Electrónica Simplificada",
                class_name="text-4xl md:text-5xl font-extrabold text-white mb-6 text-center",
            ),
            rx.el.p(
                "Conecte sus sistemas con el SII de Chile de manera segura y eficiente. Automatice la emisión y gestión de sus documentos tributarios electrónicos.",
                class_name="text-xl text-gray-300 mb-12 text-center max-w-3xl mx-auto",
            ),
            class_name="container mx-auto px-6 pt-20 pb-10",
        ),
        feature_section(
            image_src="/sii_conn/1.png",
            title="Aplicación amigable e intuitiva",
            description="Nuestra API se conecta directamente con los servicios del SII, garantizando una comunicación segura y sin intermediarios. Cumpla con todas las normativas vigentes y mantenga su información tributaria protegida.",
            reverse=False,
        ),
        feature_section(
            image_src="/sii_conn/emision.png",
            title="Automatización de Documentos Tributarios",
            description="Genere, envíe, reciba y gestione Facturas, Boletas, Notas de Crédito/Débito y Guías de Despacho de forma automática. Reduzca errores manuales y ahorre tiempo valioso para su equipo.",
            reverse=True,
        ),
        feature_section(
            image_src="/sii_conn/Diseño sin título (3).png",
            title="Dashboard de Monitoreo en Tiempo Real",
            description="Visualice el estado de todos sus documentos tributarios en un panel de control intuitivo. Monitoree envíos, aceptaciones y rechazos del SII en tiempo real, manteniendo el control total sobre su facturación.",
            reverse=False,
        ),
        feature_section(
            image_src="/sii_conn/Diseño sin título (4).png",
            title="Fácil Integración con sus Sistemas",
            description="Diseñado para ser flexible, SII Connector se integra fácilmente con su ERP, CRM o cualquier sistema de gestión existente. Ofrecemos documentación completa y soporte para una implementación rápida y sin complicaciones.",
            reverse=True,
        ),
        rx.el.div(
            rx.el.button(
                "Solicita tu demo",
                on_click=State.open_demo_form,
                class_name="bg-orange-500 text-white font-bold py-4 px-10 rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-lg hover:shadow-orange-500/40 transform hover:-translate-y-1 text-lg",
            ),
            class_name="text-center py-20",
        ),
        demo_form_dialog(),
        class_name="bg-blue-900",
    )