const themeButton = document.getElementById("theme-toggle");
const languageButton = document.getElementById("language-toggle");

if (themeButton) {
    themeButton.addEventListener("click", () => {
        document.body.classList.toggle("dark");

        const isDark = document.body.classList.contains("dark");
        themeButton.textContent = isDark ? "☀" : "☾";
    });
}

const translations = {
    en: {
        title: ["Vladyslav Hadiak | Python Developer"],
        ".nav-links a": ["Work", "About", "Contact"],
        ".greeting": ["Hi, I'm"],
        ".hero-content h2": ["Python Developer"],
        ".description": [
            "I build backend systems, automation tools and data-driven applications.",
        ],
        ".hero-buttons .primary": ["View my work"],
        ".achievement-content p": ["PLACE"],
        ".achievement-project p": ["Sole Developer"],
        ".projects .section-heading p": ["SELECTED WORK"],
        ".projects .section-heading h2": ["Projects"],
        ".about .section-heading p": ["ABOUT ME"],
        ".about .section-heading h2": ["Building with Python."],
        ".about-content p": [
            "I'm a Cybersecurity student at Lviv Polytechnic National University and a Python Developer focused on backend development, automation and data processing.",
            "I enjoy building practical software solutions and working with APIs, databases and automated systems.",
        ],
        ".contact > p": ["HAVE A PROJECT IN MIND?"],
        ".contact h2": ["Let's talk."],
        
    },
    ua: {
        title: ["Владислав Гадяк | Розробник Python"],
        ".nav-links a": ["Проєкти", "Про мене", "Контакти"],
        ".greeting": ["Привіт, я"],
        ".hero-content h2": ["Розробник Python"],
        ".description": [
            "Я створюю серверні системи, інструменти автоматизації та застосунки для роботи з даними.",
        ],
        ".hero-buttons .primary": ["Мої роботи"],
        ".achievement-content p": ["МІСЦЕ"],
        ".achievement-project p": ["Розробник"],
        ".projects .section-heading p": ["ОБРАНІ РОБОТИ"],
        ".projects .section-heading h2": ["Проєкти"],
        ".about .section-heading p": ["ПРО МЕНЕ"],
        ".about .section-heading h2": ["Створюю на Python."],
        ".about-content p": [
            "Я вивчаю кібербезпеку у Львівській політехніці та займаюся розробкою на Python, зосереджуючись на серверній розробці, автоматизації й обробці даних.",
            "Мені подобається створювати практичні програмні рішення та працювати з API, базами даних і автоматизованими системами.",
        ],
        ".contact > p": ["МАЄТЕ ІДЕЮ ДЛЯ ПРОЄКТУ?"],
        ".contact h2": ["Поговорімо."],
    },
};

function setLanguage(language) {
    const languageTranslations = translations[language];

    for (const [selector, textValues] of Object.entries(languageTranslations)) {
        const elements =
            selector === "title"
                ? [document.querySelector("title")].filter(Boolean)
                : document.querySelectorAll(selector);

        elements.forEach((element, index) => {
            if (textValues[index] !== undefined) {
                element.textContent = textValues[index];
            }
        });
    }

    const emptyProjectsMessage = document.querySelector(".project-grid > p");
    if (
        emptyProjectsMessage &&
        ["No projects added yet.", "Проєктів поки немає."].includes(
            emptyProjectsMessage.textContent.trim(),
        )
    ) {
        emptyProjectsMessage.textContent =
            language === "ua" ? "Проєктів поки немає." : "No projects added yet.";
    }

    document.documentElement.lang = language === "ua" ? "uk" : "en";
    languageButton.textContent = language === "ua" ? "EN" : "UA";
}

if (languageButton) {
    let currentLanguage = "en";
    setLanguage(currentLanguage);

    languageButton.addEventListener("click", () => {
        currentLanguage = currentLanguage === "en" ? "ua" : "en";
        setLanguage(currentLanguage);
    });
}
