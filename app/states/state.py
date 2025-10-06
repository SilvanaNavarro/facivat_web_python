import reflex as rx
import re


class Service(rx.Base):
    image: str
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

    @rx.event
    def set_page(self, page_name: str):
        self.current_page = page_name

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