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
                        "Empoderar a las empresas con soluciones tecnológicas personalizadas que impulsen su crecimiento, eficiencia y competitividad en el mercado digital. Nos comprometemos a entregar productos de alta calidad y un servicio de consultoría excepcional que genere valor tangible.",
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
                        "Ser el socio tecnológico líder y de mayor confianza para empresas en Latinoamérica, reconocidos por nuestra innovación constante, excelencia en la ejecución y un profundo entendimiento de las necesidades de nuestros clientes, liderando la adopción de inteligencia artificial y automatización.",
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