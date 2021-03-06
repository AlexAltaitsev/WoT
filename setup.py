import setuptools
# Открытие README.md и присвоение его long_description.
with open("README.md", "r") as fh:
	long_description = fh.read()

# Определение requests как requirements для того, чтобы этот пакет работал. Зависимости проекта.
# requirements = ["requests<=2.21.0"]

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
	# Имя дистрибутива пакета. Оно должно быть уникальным, поэтому добавление вашего имени пользователя в конце является обычным делом.
	name="hello_world_ericjaychi",
	# Номер версии вашего пакета. Обычно используется семантическое управление версиями.
	version="0.0.1",
	# Имя автора.
	author="Eric Chi",
	# Его почта.
	author_email="ericjaychi@gmail.com",
	# Краткое описание, которое будет показано на странице PyPi.
	description="A Hello World package",
	# Длинное описание, которое будет отображаться на странице PyPi. Использует README.md репозитория для заполнения.
	long_description=long_description,
	long_description_content_type="text/markdown",
	# URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
	url="https://github.com/ericjaychi/sample-pypi-package",
	packages=setuptools.find_packages(),
    # install_requires=requirements,
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],

	python_requires='>=3.6',
)
