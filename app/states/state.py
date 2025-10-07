import reflex as rx
import re


class Service(rx.Base):
    image: str
    description: str


class OtherServiceInfo(rx.Base):
    image: str
    title: str
    description: str


def is_valid_email(email: str) -> bool:
    pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


class State(rx.State):
    current_page: str = "home"
    services: list[Service] = [
        Service(
            image="/desarrollo_apps.png",
            description="Desarrollo de Aplicaciones a Medida",
        ),
        Service(image="/IA.jpg", description="Creación de Agentes de IA Avanzados"),
        Service(
            image="/Asesorias.jpg", description="Asesorías y Consultoría Tecnológica"
        ),
        Service(
            image="/desarrollo_software.jpg",
            description="Diseño y Desarrollo de Software a Medida",
        ),
        Service(image="/integracion.jpg", description="Integración de Procesos"),
    ]
    form_data: dict[str, str] = {}
    show_demo_form: bool = False
    active_service_index: int = -1
    show_scroll_top_button: bool = False
    other_services_list: list[OtherServiceInfo] = [
        OtherServiceInfo(
            image="/agente_ia.jpg",
            title="Crea tus Propios Agentes IA",
            description="Desarrollamos agentes de inteligencia artificial personalizados para automatizar tareas y optimizar procesos.",
        ),
        OtherServiceInfo(
            image="/cloud.jpg",
            title="Arquitecturas Modernas en la Nube",
            description="Centralizamos tus datos con el diseño e implementación de arquitecturas on-cloud escalables y seguras.",
        ),
        OtherServiceInfo(
            image="/soluciones_amedida.jpg",
            title="Aplicaciones Personalizadas",
            description="Desarrollamos aplicaciones a medida que se ajustan perfectamente a las necesidades de tu negocio.",
        ),
        OtherServiceInfo(
            image="/asesoria2.jpg",
            title="Asesorías de Proyectos",
            description="Ofrecemos asesoría con Project Managers certificados para garantizar el éxito de tus proyectos tecnológicos.",
        ),
    ]

    @rx.event
    def set_show_scroll_top_button(self, show: bool):
        self.show_scroll_top_button = show

    @rx.event
    def set_active_service_index(self, index: int):
        if self.active_service_index == index:
            self.active_service_index = -1
        else:
            self.active_service_index = index

    @rx.event
    def set_page(self, page_name: str):
        self.current_page = page_name
        self.active_service_index = -1

    @rx.event
    def open_demo_form(self):
        self.show_demo_form = True

    @rx.event
    def close_demo_form(self):
        self.show_demo_form = False

    @rx.event
    def handle_submit(self, form_data: dict):
        if not is_valid_email(form_data.get("email", "")):
            return rx.toast.error("Por favor, introduce un correo electrónico válido.")
        self.form_data = form_data
        print("Formulario de contacto recibido:", self.form_data)
        form_id = "contact-form"
        if self.show_demo_form:
            self.show_demo_form = False
            form_id = "demo-contact-form"
            yield rx.toast.success(
                "¡Solicitud de demo enviada! Te contactaremos pronto."
            )
        else:
            yield rx.toast.success(
                "¡Gracias por contactarnos! Te responderemos pronto."
            )
        yield rx.call_script(f"document.getElementById('{form_id}').reset()")