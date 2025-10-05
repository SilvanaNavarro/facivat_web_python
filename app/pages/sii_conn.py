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
            class_name="md:w-1/2 p-4",
        ),
        rx.el.div(
            rx.el.h3(title, class_name="text-2xl font-bold text-orange-500 mb-4"),
            rx.el.p(description, class_name="text-gray-300 leading-relaxed"),
            class_name="md:w-1/2 p-4 flex flex-col justify-center",
        ),
        class_name=f"container mx-auto px-6 py-10 flex flex-col {order_class} items-center gap-8",
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
            image_src="/sii_conn/Diseño sin título (1).png",
            title="Integración Directa y Segura",
            description="Nuestra API se conecta directamente con los servicios del SII, garantizando una comunicación segura y sin intermediarios. Cumpla con todas las normativas vigentes y mantenga su información tributaria protegida.",
            reverse=False,
        ),
        feature_section(
            image_src="/sii_conn/Diseño sin título (2).png",
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
                on_click=State.set_page("contact"),
                class_name="bg-orange-500 text-white font-bold py-4 px-10 rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-lg hover:shadow-orange-500/40 transform hover:-translate-y-1 text-lg",
            ),
            class_name="text-center py-20",
        ),
        class_name="bg-blue-900",
    )