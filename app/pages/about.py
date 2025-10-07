import reflex as rx


def about_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Nuestra Esencia",
                class_name="text-4xl md:text-5xl font-extrabold text-white mb-6 text-center",
            ),
            rx.el.p(
                "Somos un equipo de innovadores, desarrolladores y estrategas apasionados por transformar negocios a través de la tecnología.",
                class_name="text-xl text-gray-300 mb-12 text-center max-w-3xl mx-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        rx.icon(
                            "rocket", class_name="inline-block mr-3 text-orange-500"
                        ),
                        "Misión",
                        class_name="text-3xl font-bold text-orange-500 mb-4",
                    ),
                    rx.el.p(
                        """Nuestra misión es impulsar el crecimiento de las pequeñas y medianas empresas mediante el desarrollo de soluciones tecnológicas accesibles, intuitivas y personalizadas que faciliten la gestión de sus trámites y operaciones diarias.
Buscamos simplificar lo complejo, eliminando las barreras digitales que limitan la productividad y competitividad, a través de herramientas como sistemas de facturación electrónica, integraciones de datos y asesorías en gestión de proyectos.
Nos motiva ser un aliado estratégico para cada cliente, entendiendo sus necesidades y acompañándolos en su transformación digital, generando igualdad de oportunidades en el entorno empresarial. Queremos empoderar a las empresas con soluciones tecnológicas personalizadas que impulsen su crecimiento, eficiencia y competitividad en el mercado. Nos comprometemos a entregar productos de alta calidad y un servicio de consultoría excepcional que genere valor tangible.""",
                        class_name="text-gray-300 leading-relaxed",
                    ),
                    class_name="bg-gray-800/50 p-8 rounded-xl shadow-lg border border-blue-800",
                ),
                rx.el.div(
                    rx.el.h2(
                        rx.icon("eye", class_name="inline-block mr-3 text-orange-500"),
                        "Visión",
                        class_name="text-3xl font-bold text-orange-500 mb-4",
                    ),
                    rx.el.p(
                        """Nuestra visión es transformar la manera en que los negocios gestionan y ayudar a las empresas a hacer crecer sus operaciones, ofreciendo soluciones tecnológicas que simplifiquen procesos, fomenten la innovación y generen igualdad de oportunidades en el entorno empresarial.
                            Aspiramos a ser reconocidos como una empresa confiable, creativa y visionaria, que impulsa el desarrollo digital de los negocios y contribuye al progreso económico y social.
                            Queremos construir un futuro donde la tecnología sea una herramienta accesible para todos, facilitando el crecimiento sostenible y la competitividad de las empresas en un mundo cada vez más digital.Queremos ser el socio tecnológico líder y de mayor confianza para empresas en Latinoamérica, reconocidos por nuestra innovación constante, excelencia en la ejecución y un profundo entendimiento de las necesidades de nuestros clientes, liderando la adopción de inteligencia artificial y automatización en tus procesos.""",
                        class_name="text-gray-300 leading-relaxed",
                    ),
                    class_name="bg-gray-800/50 p-8 rounded-xl shadow-lg border border-blue-800",
                ),
                class_name="grid md:grid-cols-2 gap-10",
            ),
            class_name="container mx-auto px-6 py-20",
        ),
        class_name="bg-blue-900",
    )