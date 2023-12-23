from io import BytesIO
import base64

def create_report_file(excel_data):

    template = f'''
    Дата - {excel_data[0]}

    Тренувальна програма -
    Тиждень -

    🟢 Блок 1 Харчування
    - загальна мета на тиждень:
    {excel_data[2]}

    Коментар по розділу ⤵️
    1 Сміттєва їжа в харчуванні: {excel_data[3]}
    2 Комфорт місця прийому їжі: {excel_data[4]}
    3 Оточення люди під час їжі: {excel_data[5]}
    4 Гаджети під час їжі: {excel_data[6]}
    5 Увага на їжі: {excel_data[7]}
    6 Емоції під час їжі: {excel_data[8]}

    Аналітика
    Середня кількість на день
    Білків - {excel_data[9]}
    Жиров - {excel_data[10]}
    Вуглеводів - {excel_data[11]}
    ККАЛ - {excel_data[12]}

    Ваші вимірювання кг/см –
    вкажіть різницю +- порівняно з попередніми
    1. Вага - {excel_data[14]}
    2. Плечі - {excel_data[15]}
    3. Груди - {excel_data[16]}
    4. Рука права - {excel_data[17]}
    5. Рука ліва -  {excel_data[18]}
    6. Талія - {excel_data[19]}
    7. Стегна – {excel_data[20]}
    8. Стегна праве - {excel_data[21]}
    9. Стегна ліве - {excel_data[22]}

    Продублюйте схему своїх добавок
    1 {excel_data[24]}
    
   
    

    🟢 Блок 2 Відновлення
    - загальна мета на тиждень:
    1 {excel_data[25]}
    
    

    Коментар по розділу ⤵️
    1 Ранковий ритуал: {excel_data[26]}
    2 Сон: {excel_data[27]}
    3 Фізичний стан: {excel_data[28]}
    4 Психічний стан: {excel_data[29]}
    5 Концентрація увага:{excel_data[30]}
    6 Травми: {excel_data[31]}

    🟢 Блок 3 Тренувальний
    - загальна мета на тиждень:
    1. {excel_data[32]}


    Коментар по розділу ⤵️
    1 Підготовка до тренування: {excel_data[33]}
    2 Загальна розминка: {excel_data[34]}
    3 Основне тренування: {excel_data[35]}
    4 Техніка виконання: {excel_data[36]}
    5 Настрій на тренуванні: {excel_data[37]}
    6 Гаджети на тренуванні: {excel_data[38]}

    🟢 Блок 4 Розвиток
    - загальна мета на тиждень:
    1 {excel_data[39]}
   
    

    Коментар по розділу ⤵️ (4.1)
    1 Розпорядок дня за годинами: {excel_data[40]}
    2 Ранковий настрій афірмація: {excel_data[41]}
    3 Посмішка протягом дня: {excel_data[42]}
    4 Подяка протягом дня: {excel_data[43]}
    5 Щирість позитивного стану 1/10: {excel_data[44]}
    6 Спостереження світу: {excel_data[45]}
    7 Відчуття дзеркала світу 1/10: {excel_data[46]}
    8 Аналіз свого кола спілкування: {excel_data[47]}
    9 Добрі справи: {excel_data[48]}
    10 Добрі справи для тварин: {excel_data[49]}
    11 Добрі справи для рослин: {excel_data[50]}
    12 Добрі справи недобрим людям: {excel_data[51]}
    13 Навичка радіти невдачам: {excel_data[52]}
    14 Не добрі справи: {excel_data[53]}
    15 Нові знання: {excel_data[54]}
    16 Читання книг: {excel_data[55]}
    17 Нові навички: {excel_data[56]}
    18 Передача свого досвіду: {excel_data[57]}
    19 Творча робота: {excel_data[58]}
    20 Робота з душею 1/10: {excel_data[59]}

    21 Сприйняття Світу:
    - 21.1 боротьба із створеними ситуаціями: {excel_data[60]}
    - 21.2 довіра до створених ситуацій: {excel_data[61]}

    22 Фільтр негативних думок:
    кількість - причина
    - 22.1 волоцюги некеровані думки: {excel_data[62]}
    - 22.2 злі помисли: {excel_data[63]}

    23 Фільтр чистоти свідомості:
    - 23.1 думки: {excel_data[64]}
    - 23.2 емоції: {excel_data[65]}
    - 23.3 дії: {excel_data[66]}

    24 Наповнення образу своєю увагою:
    - 24.1 довгострокова мета: {excel_data[67]}
    - 24.2 список рейтинг пріоритетів: {excel_data[68]}
    - 24.3 розуміння від точки А до точки Б: {excel_data[69]}

    Особистий день: https://t.me/+m3us-GADQkc1M2Ni

    ✅ Підсумок
    Дайте оцінку своїй роботі - опишіть як бачите ⤵️
    {excel_data[70]}


    Відправити мінімум раз на тиждень 
    - день свого харчування 
    https://t.me/athletfood

    Запитання тренеру на будь-яку тему 
    https://t.me/+lfMlTDuDBX01MjIy'''

    
    return template

def create_stat_message(statistics: dict) -> str:
    message = ""

    for key, value in statistics.items():
        message += f"{key}:\n"
        for stat_type, stat_value in value.items():
            if isinstance(stat_value, dict):
                message += f"  - {stat_type}:\n"
                message += f"    - Min: {stat_value.get('min', 'N/A')}\n"
                message += f"    - Max: {stat_value.get('max', 'N/A')}\n"
                message += f"    - Avg: {stat_value.get('avg', 'N/A')}\n"
                # Check if 'plot_path' key exists in the dictionary
                if 'plot_path' in stat_value:
                    # Embed the plot as a base64-encoded image in the HTML message
                    plot_path = stat_value['plot_path']
                    plot_image = generate_base64_plot(plot_path)
                    message += f"    - Plot: {plot_image}\n"
            else:
                # Handle cases where stat_value is not a dictionary
                message += f"  - {stat_type}: {stat_value}\n"

        message += "\n"

    return message

def generate_base64_plot(plot_path):
    # Read the plot image
    with open(plot_path, "rb") as plot_file:
        plot_data = plot_file.read()

    # Encode the image data as base64
    base64_plot = base64.b64encode(plot_data).decode("utf-8")

    # Create an HTML image tag with the base64-encoded image
    plot_image = f"<img src='data:image/png;base64,{base64_plot}'/>"

    return plot_image