# Определение персонажей игры.
define e = Character('Эмили', color="#f3f35d")

define j = Character('Джек', color="#850693")

define br = Character('Капитан Браун', color="#6a5009")

define al = Character('Алекс', color="#07ad07")

define an = Character('Анна', color="#5660b9")

define h = Character('Харпер', color="#b02c17")

define r = Character('Рроберт', color="#a0a5a0")


#Музыка и звуки

define audio.galaxy_start = "audio/galaxy_start.mp3"
define audio.horror_moment = "audio/horror_moment.mp3"

#Переменные 

define lab = False

define lid = False

define ostat = False

define leave = False

define yun_spas = False

define vsled = False

define ulet = False

# Сцена 1: Вступление

# 1.Представление главного героя Джека и его коллеги Эмили
label start:

    play music galaxy_start
    scene bg_ship_room

    "На просторах вселенной в немом ожидании застыл космический корабль."

    "И это ожидание было прервано криком."

    play sound horror_moment
    e "Джек, смерть идет за тобой, УАХАХА!!!"

    show jack at left

    j "Значит я ей сильно нравлюсь. А вообще, хватит орать, мешаешь работать."

    "Джек склонился над планшетом, читая передовые научные сводки в области биотехнологий."

    j "Мда, никаких рецептов бессмертия на сегодня. Только рецепты котлет из саморастущего марсианского мяса."

    show emily at right
    with dissolve
    e "Как второй научный сотрудник этого корабля и твоя коллега, в свете надвигающегося завтрака я вынуждена сообщить о приоритете котлет над бессмертием!"

    "Заметив, что Джек никак не отреагировал, Эмили начала громко зевать и сопеть через разные интервалы."

    j " В самом деле, пошли на кухню."

    hide emily_new
    hide jack

    scene bg_ship_kitchen
    with fade

    "На кухне двух сотрудников встретил запах яичницы и крепкого кофе, хотя ни того ни другого не удалось обнаружить."

    stop music fadeout 1.0

    jump first_2    

    return

# 2.Установление цели Джека достичь бессмертия.
label first_2:

    j "Ага, значит капитан уже проснулся." 

    "Пока Эмили начала готовить завтрак, Джек, подавив зевоту, взглядом впивался в свой планшет."

    e "Что-то новое раскопал насчет этой планеты?"

    menu:
        "Включиться в разговор.":
            "Пока не особо. Но проект и по первичным данным многообещающий."


        "Проигнорировать.":
            e "Ясно, занятой человек."
            "В глубинах электронного архива вы обнаруживаете заметку о том, что планета X вероятна названа так в честь
            гигантских каменных сооружений, занимающих центральное место в мифологии местных племен. "

    j "Вообще, эта планета самая настоящая находка для меня."

    e "Я чего-то не знаю."

    j "Последняя группа колонистов с этой планеты прислала останки погребенных 50 лет назад коренных жителей планеты. Некоторым жителям на момент захоронения было по тысяче лет."

    e "Это какая-то продвинутая технология консервации?"

    j "Нет, это Спарта." 

    j "На самом деле мертвых хоронят сразу же после смерти. А значит они раскрыли как минимум экстремального долголетия, а может быть и физиологического бессмертия!"

    e "Ага, и ты как ярый сторонник продления человеческих страданий хочешь этот секрет заполучить..."

    j "Конечно! Как минимум, будучи бессмертным, я смогу бесконечно исследовать вселенную в поисках других планет с однобуквенными названиями!"

    j "К сожалению, условия на планете очень суровые, иначе Земля бы плотно занялась ею, а я бы быстрее добрался сюда."

    jump first_3

    return

# 3.Введение капитана Брауна и объяснение миссии отправки команды на чужую планету.
label first_3:

    "Разговор прерывается звуком  тяжелой солдатской поступи."

    br "Утро, халатики."

    "Капитан Браун ловко выхватывает у Эмили кружку с кофе и осушает половину одним мощным глотком."

    j "Капитан, у вас кадык как затвор пистолета двигается. Вам бы к врачу."

    br "То ли еще будет... Итак, товарищи, вы на пороге к осуществлению мечты каждого ученого - прилететь в неизвестную никому дыру и копаться в тамошней грязи до посинения!"

    e "Так точно."

    br "К вашему глубочайшему сожалению, просто так покопаться в грязи нельзя. Последняя команда колонистов уже пять месяцев не выходит на связь."

    j "Это говорит о том, что..."

    br  "Это говорит о том, что мы можем ожидать всего плохого. Так что с вами отправится разведывательный отряд во главе с вашим знакомым офицером Алексом. Его рейс в соседнюю систему отменен."

    j  "...иии...?"

    br "...иии это все. Я спать."

    "С этими словами капитан отхлебнул кофе из кружки Эмили, сел на стул, сдвинув фуражку на нос, и усиленно засопел."

    jump second_1

    return


#Сцена 2 : Путешествие к чужой планете

#1.Представление членов команды, включая Алекса

label second_1:

    "Подходил к концу последний день перед высадкой на планету X."

    "Алекс в очередной раз пересобирал свое оружие и обмундирование. Члены его разведывательного отряда молча повторяли тот же ритуал."

    "Эмили, в свою очередь, перепроверяла наличие всех нужных гаджетов - мультифункциональных датчиков, сканеров, гравитационных компенсаторов и еще кучи штук, так необходимых для копания в грязи."

    menu:
        "Подойти к Алексу.":
            j "Ты разве что артиллерийскую батарею на корабль не притащил."
            al "Ты сильно удивишься когда мы спустимся на землю."
            "Звонкое мужское рукопожатие разрезает воздух."
            j "Рад видеть. Много вас значит."
            al "Двадцать человек, включая меня."
           


        "Поприветствовать Эмили.":
            e "О, Джек. У меня защитный костюм не сходится, помоги страждущему."
            j "Спасение утопающего в жире дело рук..."
            e "Старший научный сотрудник должен знать, что жир науке - не помеха."
            "\"Тоже верно\" - сказал Джек и резко затянул молнию на защитном костюме."
            e "Спасибо... буду налаживать дыхание... в условиях стесненной атмосферы."

    "Алекс, закончив свой ритуал, резво спрыгивает на скамейку и начинает декламировать отрывистым голосом:"

    al "Спасение колонистов  является внеочередной задачей для разведывательного отряда \"Наск 21\". Отряд должен разведать территорию колонии и окрестных племен."

    al "Каждые три дня отряд должен направлять рапорт о произведенных действиях в Единую Коммуникационную Систему."

    "Алекс спрыгнул со скамейки,выдержал театральную паузу и пробормотал: "

    al "Ужин..."

    "Отряд профессиональных разведчиков, урча животами, ломанулся в двери отсека."

    jump second_2

    return

#2.Показ пейзажей во время полета в космосе
label second_2:

    "Последние часы перед посадкой особенно ценны."

    "Вроде кажется, что пустота космоса вконец осточертела."

    "Но только приближаясь к планетам или к каким-то другим каменным шарикам, ты понимаешь, чем наполнена эта самая пустота."

    "Вечностью." 

    "Если сознание касается этой вечности своим взором, то сразу же возникает желание стать похожим или побороться с ней - в общем, тем или иным способом приобщиться к силе, которая не подвержена  распаду как все остальное."

    "С этими мыслями Джек обращает свой взор на планету, благо корабль подлетел на достаточное расстояние для того, чтобы лицезреть вид очередного каменного шарика."

    "Жаркий климат с относительно небольшим количеством влаги породил засушливые пустыни и полупустыни с редкими полосками тропического леса."

    "И такой была вся планета. За исключением ряда циклопических каменных сооружений, что покрывали значительную ее часть."

    "Ретранслятор в ухе Джека прожужжал и Джек направился на капитанский мостик."


    jump second_3

    return

#3.Обсуждение плана Джека на чужой планете
label second_3:

    br "Итак, дражайшие мои коллеги по опасному ремеслу. Готов запротоколировать ваш согласованный план перед отправкой."

    al "Без этого никак не..."

    br "Никак нет, лейтенант. Особенно это касается пункта об ответственности за ваши жизни."

    br "Вы сходите с корабля, а значит с меня взятки гладки. Вы говорите, а я пока развалюсь на диване, диктофон пишет."

    "Капитан разваливается на диване."

    j "План такой - мы все высаживаемся на месте последней колонии. Далее я вместе с Эмили направляюсь на территорию племен, проживающих рядом с каменными сооружениями."

    j "Если на месте колонии не будут обнаружены колонисты, то Алекс двигается дальше вместе с нами - к племенам, как я и сказал."
    
    j "В обоих случаях - и в колонии, и у племен мы с Эмили проводим исследование грунта, предметов быта и прочее, а Алекс занимается поисковой деятельностью."

    " \"Объединение наших усилий должно стать оптимальной стратегией в целях реализации интересов обеих групп\" - канцелярски подытожил Алекс."

    " \"Ну и все\", - отрыгнул капитан Браун - \"По коням.\""

    jump third_1

    return


#Сцена 3 : Прибытие на чужую планету

#1.Представление Анны, местной жительницы планеты, которая помогает команде Джека
label third_1:

    " Приземлившись, команда исследователей и разведчиков обнаруживает пустое поселение."

    " Разбитые окна домов-палаток, обломки стен и детали разнообразных стационарных сенсоров - поселение встречает отряд угрюмо и неприветливо."

    " Вдруг слышится крик - совсем недалеко."

    "Разведчики занимают оборонительные позиции."

    "К отряду приближается женщина в набедренной повязке."

    an "Меня зовут Анна. Странники, способны ли вы оказать помощь моему брату? Вот уже 4 дня он истекает кровью в развалинах чужеземного дома."

    "Члены  отряда многозначительно переглядываются. Джек, Эмили и Алекс кивают друг другу."

    al "Решение принято. Выдвигаемся вслед за женщиной. Всем держаться начеку." 

    "Отряд пробирается к развалинам дома в северной части поселения."

    "На полу, пронзенный железным штырем, лежит юноша с серой кожей. Кровь медленно стекает из его туловища в уже засохшие красные лужи."

    "Юноша явно в сознании, но он молчит,  наблюдая за вами с гримасой боли."

    menu:
        "Спасти юношу из ловушки, используя гидравлический транслятор.":
            $ yun_spas = True
            "Гидравлический транслятор мощным импульсом поднимает юношу над штырем."
            "Юноша падает в руки четырех разведчиков. Анна перехватывает своего брата."
            an "Благодарю вас, странники."


        "Отрезать штырь с обратной стороны плазменным резаком и перенести истекающего юношу в таком виде на корабль.":
            $ yun_spas = False
            "Штырь отрезан. Юноша вместе с ним заваливается набок."
            "Разведчики подхватывают его и уносят на корабль."
            an "Вы можете вытащить его?"
            "Сначала нужно провести исследование такого странного феномена."

    jump third_2

    return

#2.Установка базового лагеря на планете и проведения исследований:
label third_2:

    "Анна удаляется от отряда в северном направлении."

    al "Мдааа... с радужной ноты все начинается."

    e "Джек, как тебе идея быть бессмертным, вечно истекая кровью?"

    j "Надо просто смотреть куда падаешь. Обувь хорошую купить еще, чтоб не поскользнуться..."

    "После неудачной шутки повисает пауза  и члены отряда расходятся устанавливать базовый лагерь."

    "Разведчики и исследователи совместно собирают и размещают дома-палатки, а также системы сенсоров, слежения и видеонаблюдения."
    
    "Разведчики начинают укреплять дома дополнительными бронелистами, в то время как у Джека и Эмили остается пара часов на проведение исследования."

    j "Ты займись грунтом, а я соберу биоматериал с вещей и поверхностей."

    e "Будет сделано. Только не разбей ничего."

    j "Смешно. Я оценил."

    "Два часа раскопок проходят безрезультатно. Джек, в свою очередь, находит следы каких-то биологических жидкостей на уцелевшей утвари в одном из домов."

    if yun_spas == False:
        "Ученые поднимаются на корабль и проходят в медицинский отсек."
        "Юноша лежит, безмолвно рассматривая интерьер отсека сквозь гримасу боли."
        "Джек пытается позвать юношу, но тот никак не реагирует. Тогда Джек берет образцы крови и эпителия у юноши."
        j "Можем доставать."
        "Джек при помощью гидравлического транслятора выдавливает штырь из тела раненого. Затем он погружает юношу в медикаментозный сон."
        e "Пора и нам отдохнуть."

    "Наступившая ночь застает исследователей в их новообретенном жилище."


    jump third_3

    return

#3.Установление контакта с Робертом, бессмертным колонистом на планете:
label third_3:

    "Ранним утром следующего дня к краю лагеря подходит Анна, вызывая вой сигнальных систем."

    "Отряд, щурясь от неожиданно яркого солнца, выходит поприветствовать гостью."

    "Разведчики приветливо держат оружие наготове."

    if yun_spas == False:
        e "Сейчас приведем вашего брата. Похоже в его организме какие-то совершенно удивительные ткани."
        "Джек приводит юношу к Анне. Отверстие в груди до конца не заросло, но он, тем не менее, не говоря ни слова, начинает удаляться от лагеря в северном направлении."

    j "Знаете, Аристотель говорил, что философия начинается с удивления. В этом отношении философия - мать и отец всех наук." 

    j "Ваш брат -  это что-то удивительное."

    an "Вы ищете своих бывших сородичей, чужеземцев."

    e "Почему бывших? Они мертвы?"

    an "Большая их часть жива."

    j "А что случилось с меньшей?"

    an "Убили свои же."

    al "Безоговорочно верим."

    an "Тут вера не нужна. В любом случае, вам нужно встретится с одним из  безвременных."

    j "?"

    an "Идем."

    "Пожав плечами, члены отряда начали продвигаться на восток от города вслед за женщиной."

    "Внезапно им перегородил дорогу высокий мужчина с серой кожей."

    r "Безвременный Роберт ожидает странников."

    jump fourth_1

    return

#Сцена 4 : Враждебные встречи

#1.Представление Харпера и его группы, которые начинают нападать на команду Джека.
label fourth_1:

    "Из зарослей в сторону Джека летит плазменный разряд. Джек не успевает отреагировать, но разряд поглощается землей в метре от него."

    h "Солдаты или кто вы там, сложите оружие и никто не пострадает!"

    j "Кто это говорит? Мы не враги жителям этой планеты"

    "\"Засада. Код 13.\" - прошептал в радиотранслятор Алекс."

    "Все члены отряда синхронно активируют энергощиты и начинают стремительно занимать оборонительные позиции."

    h "Я - Харпер, лидер последних колонистов. Опустите оружие. Это приказ, лейтенант!"

    h "Даю пять секунд!"

    "\"Вызываем Брауна и отступаем к лагерю.\" - прошептал в радиотранслятор Алекс."

    j "У нас задание. Мы прибыли за вами, не стреляйте."

    "Отряд Джека начинает медленно отступать."

    h "Я знаю,  что вы пришли за нами."

    jump fourth_2

    return

#2.Проведение сражения и сохранение Алексом жизни Джека.
label fourth_2:

    "Плотный бластерный огонь накрывает отряд."

    "Энергетические щиты пятерых разведчиков не выдерживают и они падают замертво."

    "Остолбенев, Джек получает один разряд, второй, третий. Индикатор щита жалобно пищит на руке."

    al "Джек, пригнись."

    "Алекс сбивает Джека с ног, выпуская дымовые шашки из наплечных модулей."

    "Под прикрытием дыма весь отряд вместе с очнувшимся Джеком спешно отступает к лагерю."

    "Из дыма выходят соратники Харпера, одетые в потрепанную одежду колонистов."

    al "Залп."

    "Мощный бластерный огонь пролетает сквозь плоть и дым, оставляя на земле тела последних колонистов."

    br "Залп."

    "Из-за облаков над лагерем появляется транспортный корабль Брауна." 
    
    "Его малокалиберные лазерные турели, раскрутившись, дают очередь по соратникам Харпера, навсегда прижигая их к земле."

    "Огонь затихает. Отряд выжидает пока рассеивается дым."

    "Сорок трупов остается на земле после битвы. Харпера и Роберта среди них не обнаружено."

    "Отряд, выставив часовых, собирается в лагере, чтобы обсудить произошедшее."


    jump fourth_3

    return


#3.Обнаружение подземного города, где живут колонисты.
label fourth_3:

    e "Это какой-то бред. Нас послали сюда, чтобы их спасти, а они стремятся нас убить. Они точно не могли нас спутать с каким-то местным племенем или..."

    al "Да, он точно опознал мои шевроны."

    j "Он сказал, что знает зачем мы здесь. В любом случае, нам нужно что-то предпринять."

    al "Верно, если мы займем здесь оборону, то они рано или поздно выкурят нас. Раз это действительно колонисты, то у них могут быть средства обхода датчиков и сенсоров в лагере."

    al " Вероятно стоит перейти в тактическое наступление. На корабле Брауна слабые сенсоры, но мы можем использовать его в качестве наступательной артиллерии, дав наводку."

    e "Мы обязаны разузнать, что именно заставило их палить по нам!"

    al "Я похороню своих и мы пойдем."

    menu:
        "Отправиться в погоню за Харпером":
            $ vsled = True
            "Алекс одобрительно кивает."
            "Отряд движется по следам отряда Харпера, используя оптический камуфляж."
            "Вдруг Джек замечает тело одного из последних колонистов."
            "Над телом громадиной нависает Роберт с копьем в руке."

        "Попытаться продолжить исследования, отправившись к каменным сооружениям.":
            $ vsled = False
            j "Не взирая на потери, мы должны отправится к нашему основному пункту исследования."
            al "Не одобряю твоего решения, но, по крайней мере, мы не будем стоять на месте."
            "Отряд выдвигается на север."
            "Каменные сооружения возвышаются над землей, как бы угрожая всему сущему своим величественным видом."
            "Эмили обнаруживает в камнях рядом с сооружениями жилу со странной красной субстанцией, напоминающей кровь."
            "Джек и Эмили берут образцы неизвестной субстанции."
            "Навстречу отряду выходит Роберт с копьем в руке."

    jump fifth_1

    return

#Сцена 5 : Новые открытия
#1.Встреча с Робертом и другими колонистами
label fifth_1:

    al "Никаких движений и слов, иначе я застрелю тебя!"

    "Роберт ударяет тупым концом копья по камню."

    "Пол под ногами членов отряда Джека начинает стремительно ехать вниз."

    "Алекс открывает огонь по Роберту, но перед ним возникает мощный энергетический щит."

    "Разряды бластера не наносят ему никакого вреда"

    j "Так, мы проехали уже где-то 300 метров...Эмили, ты считаешь?"

    e "Сенсор почему-то не работает..."

    "Вдруг земля останавливается."

    "Перед взором Джека предстает большая круглая комната с бесчисленным количеством входов и выходов."

    "Энергетический щит перед Робертом растворяется. В комнату начинают прибывать люди с обычной и серой кожей."

    jump fifth_2

    return


#2.Обсуждение того, как создать новую цивилизацию на планете.
label fifth_2:

    r "Итак, все в сборе. Явились чужеземцы, дабы построить еще один рассадник насилия и безумия?"

    al "Похоже мы явились за теми, кто рассаживает насилие и безумие..."

    r "Значит на на одной стороне мы."

    "Роберт убирает копье убирает копье, прикрепив его на стену."

    "Заполонившую комнату люди достают ножи из-под одежды и открыто убирают их в ножны."

    j "Ладно, это все  очень интересно, но я хотел вот что спросить."

    j "Роберт, ты бессмертен?"

    r "Да, как и все безвременные. Сила сия дарована нам этими священными каменными сводами."

    r "К сожалению, сила не освещает всех собою. Часть значительная нашего народа смертна и скоротечна."

    r "Их смерти парализуют общество наше. Мы скованы рыданием и скорбью."

    j "Хм...может эти камни аки маяк указали мне путь на вашу планету и я смогу... ну не знаю... помочь вам?"

    "Лицо Роберта приобрело глубоко задумчивый вид."

    e "Какую помощь ты хочешь им предложить?"

    menu:
        "Мне нужна мощная лаборатория, где я смогу подробно изучить этот удивительный феномен \"безвременности\"":
            $ lab = True
            r "Так тому и быть. Мы направим на деяние это все силы свои."

        "Организовать экспидицию вглубь каменных сооружений, попутно обучая племя исследовательскому делу.":
            $ lid = True
            r "Хорошо придумано. Мы отправимся за тобой, посланник камней."

    jump fifth_3

    return

#3.Установление новой базы для команды Джека и начало строительства.
label fifth_3:

    "Роберт начинает проводить мобилизацию ресурсов и населения племени."

    "Проблеск энтузиазма в головах людей на время заглушает стенания и молчаливый траур."

    j "Как глубоко под землей мы находимся?"

    r "Никто не знает. Но лифты каменные либо поднимаются на поверхность либо  опускаются до поселения."

    j " Есть ли еще какие-то способы проникнуть сюда?"

    r "Тысячелетние тоннели под нами."

    j "Это всё?"

    r "Да."

    j "Что ж, вероятно, Харпера можно не ждать."

    if lab == True:
        "В течение месяца отряд Джека и подземные жители  сооружают лабораторию."
        "В ход идут и вещи, украденные у людей Харпера - с каждым колониальным кораблем всегда отправляется научное оборудование."

    if lid == True:
        "В течение месяца отряд Джека и подземные жители  подготавливают экспедицию в древние тоннели."
        "Джек и Эмили обучают жителей обращению с исследовательскими сенсорами и датчиками."

    jump sixth_1


    return

#Сцена 6 : Восстание Харпера 

#1.Нарастание напряжения между командой Джека и Харпером

label sixth_1:

    "В один из дней прямо перед Джеком появляется голограмма Харпера."

    h "Джек, ты должен улететь с этой планеты и забыть про нас навсегда."
    j "Как ты проник сюда?"

    h "Неважно, я выполняю задание правительства, ты должен прекратить попытки препятствовать мне."

    j "Ты точно обезумел. Именно правительство направило сюда разведывательный и исследовательский отряды."

    h "Мое задание секретно. Я связан с высшими военными чинами. То, что мы здесь обнаружили..."

    j "Так?"

    h "Эти существа - безвременные, совершенно удивительные. Они обладают опытом целых столетий. Они могут стать идеальными солдатами и главнокомандующими армией."

    h "Даже при нынешнем состоянии их общества они легко адаптируются к любой ситуации - их реакция лучше обычной человеческой, а ловкость и скорость движений на высоте."

    h "Может их разум и омрачен сейчас, но их мышечная память безупречна."

    j "Время?"

    h "Даю день на обдумывание."


    jump sixth_2


    return

#2.Попытка Харпера захватить базу и использовать бессмертие в своих целях.

label sixth_2:

    al "Джек, если Харпер смог разместить здесь свою голограмму, то значит... завелась крыса."

    j "Отдавай приказ об укреплении позиций, я расставлю сенсоры."

    al "Будет сделано."

    "Алекс кричит, призывая всех торопиться. Жители встревожены - они не ожидают нападения под священными сводами."

    "Проходит день. Джек прильнул к экрану Сенсора. Харпер должен сделать свой ход."

    "Внезапно стены вокруг отряда Джека опускаются - это каменные лифты."

    "Из лифтов выбегают последние колонисты. Отряд Джека попадает под перекрестный огонь."

    al "Подрыв!"

    "Десятки дымовых шашек взлетаю из-под пола комнаты. Плотный дым окутывает всех присутствующих."

    "\"Отдай мне результаты исследований и улетай с планеты целым!\" - кричит Харпер где-то в дыму."


    jump sixth_3


    return


#3.Решение Джека остаться на планете и бороться против Харпера.

label sixth_3:

    "Перестрелка превращается в рукопашную схватку. Жители держат основной удар на себе."

    "Внезапный хлопок и дым уходит - рассеивающий динамит!"

    "Пятившиеся последние колонисты отбрасывают подземных жителей и начинают в упор их расстреливать."

    "Разведчиков мало, а жители вооружены лишь старыми плазменными винтовками. Враги все сильнее теснят их к южной части комнаты."

    "Алекс показывает Джеку на южный выход из зала."

    "Прикрытый огневой поддержкой, Джек срывается с места и бежит к выходу."

    "Эмили, отстреливаясь, следует за ним."

    "Через 5 минут исследователей догоняет Алекс в сопровождении своих разведчиков. Их осталось всего 8."

    e "Рано или поздно Харпер нас найдет."

    al "Валить отсюда надо! Пока живы..."

    menu:
        "Остаться и сражаться с Харпером. Попытаться перебить его отряды по одному.":
            $ ostat = True
            e "Возможно мы успеем кого-нибудь спасти."

        "Попытаться найти выход на поверхность.":
            $ leave = True
            al "Будем надеяться, что лифты не заблокированы."

    jump seventh_1

    return

#Сцена 7 : Конец Акта 1 

#1.Смерть Алекса в битве с Харпером

label seventh_1:

    "Отряд ускоренным шагом двигается прочь от зала."

    "Очередь из плазмогана останавливает отряд посередине узкого коридора. Двое разведчиков падают замертво."

    "Харпер предстает перед отрядом, облаченный в военный экзоскелет."

    h "Если вам это поможет, то я не хотел вашей смерти. Я не маньяк или безумец. Я просто исполнял приказ."

    al "Да, нам сильно поможет то, что ты  вербально выписал себе индульгенцию. Какой в этом вообще смысл?" 

    al "Код 1000. Красный."

    menu:
        "Подчиниться команде Алекса и отступить.":
            pass

        "Спасти Алекса, забрав Харпера с собой в могилу.":
            "Джек отталкивает Алекса в сторону и мчится прямо на Харпера."
            "Выстрелы раскрученного плазмогана один за другим попадают в энергетический щит Джека, переполняя его."
            "В последний момент перед опустошением щита Джек падает к ногам Харпера и  деактивирует щит, направив накопленную от выстрелов энергию во все строны."
            jump death

    "Выжившие члены отряда, все, кроме Алекса, побросав оружие, начинают убегать в противоположную от сражения сторону."

    "Джек, обернувшись, видит как рюкзак Алекса трансформируется в миномет."

    "Алекс дает залп по потолку и каменные своды обрушиваются. Гигантские куски камней погребают под собой Алекса и Харпера."

    "Потеряв своего командира, отряд последних колонистов перестают преследовать команду Джека."

    "Поняв, что Харпер уже точно не выйдет на связь, они пытаются лихорадочно найти выход из подземного поселения."

    "Но все лифты заблокированы и последние колонисты становятся легкой добычей для подземных жителей."

    jump seventh_2

    return

#2.Джек осознает, что его мечта о бессмертии может привести к опасным последствиям.

label seventh_2:

    "На следующий день после битвы подземные жители скорбят по погибшим, издавая душераздирающие вопли и дикий плач."

    "Последствия вчерашнего нападения уже устранены."

    "Поредевший отряд Джека собирается в главном зале вместе с Роберт обсудить произошедшее."

    j "Почему они вообще потеряли связь с учетом того, что сказал Харпер про его правительственное задание?"

    j "Сомневаюсь, что он врал. И тем более он не был похож на безумца."

    r "Верно все. Оборвали мы связь, дабы не позволить им злодеяние свершить."

    e "Значит остается лишь похоронить погибших и вернуться к проекту..."

    j "Да. И каким-то образом не допустить сюда еще каких-нибудь исполнителей особо интересных приказов..."

    j "...Какой, однако, чудовищный во всех смыслах интерес вызывает эта \"безвременность\"."

    j "В отчете объяснить еще потерю личного состава...мда..."

    e "Будем надеяться, что своим трудом отыграем хотя бы малую часть их жертвы..."



    jump seventh_3

    return

#3.Открытие новых технологий и возможностей на чужой планете.

label seventh_3:

    "Получив возможность беспрепятственно вести свои исследования, Джек и Эмили совершают множество открытий."

    "Секрет поразительного долголетия серых жителей планеты - жилы в \"священном \" камне."

    "Воздействуя на материнский плод в чреве матери своими эманациями, камень вызывает серьезную мутацию."

    "Эта мутация приостанавливает процесс старения в организме и дает поразительную регенерацию многим тканям."

    "Однака, ни Джек ни Эмили не находят способ, с помощью которого можно было бы управлять такой силой."

    e "С таким оборудованием это все, что мы можем. Что ты собираешься делать?"


    menu:
        "Остаться и продолжать исследования дальше, сконструировав более мощное оборудование.":
            if yun_spas == False and lid == True:
                jump best_end
            "Джек вместе c Эмили остается на планете."
            "Джек и его команда работают вместе с жителями планеты, чтобы создать новые технолоогии."
            "Технологии, которые позволят преодолеть тяжелые условия проживания на планете и использовать ее ресурсы более эффективно."
            "Джек понимает, что бессмертие - это не единственное, что имеет ценность. Важно сохранить жизнь на планете и заботиться о ее будущем."


        "Пора улететь с планеты X и хорошенько всё обдумать.":
            if yun_spas == False:
                jump alone
            e "Хорошо. Надо выбраться на поверхность и вызвать Брауна."
            "Джек не смог найти способ достижения бессмертия и оставляет свои исследования, считая их безнадежными."
            "Он возвращается на Землю и начинает жить обычной жизнью, но его опыт на чужой планете засталяет его задуматься о ценности жизни."
            "И о том, какие изменения он может внести в свою жизнь, чтобы сделать ее более значимой."
            "Джек начинает по-другому смотреть на свою жизнь и окружающих его людей, и понимает, что жизнь - это не только продолжительность, но и качество."

    return


label death:
    "Джек и его команда борются на чужой планете, чтобы защитить жителей от нападений последних колонистов."
    "В результате, Джек и его команда сталкиваются с сильным противником, и Джек понимает, что он должен пожертвовать своей жизнью, чтобы защитить жителей."
    "Он умирает, зная, что его исследования и борьба были на благо других."
    return

label alone:
    "Джек находит способ покинуть планету и возвращается на Землю, гед продолжает свои исследования над достижением бессмертия."
    "Он чувствует облегчение из-за того, что оставил проблемы жизни на чужой планете."
    "Однако, спустя несколько лет Джек начинает понимать, что бессмертие может привести к одиночеству и потере ценности жизни."
    "Он понимает, что его исследования не должные приводить к отрицательным последствиям и начинает работать над технологиями, которые помогут находить людям мысл и радость в своей бессмертной жизни."
    return

label best_end:
    "Джек и его команда сотрудничают с бессмертными жителями на чужой планете, чтобы создать новую цивилизацию."
    "Они преодолевают проблемы, которые возникают на их пути и создают новый мир."
    "Мир, где бессмертие стало не только способом продлить жизнь, но и возможностью для роста, развития и достижения большего."
    return


label introduction:

    # Показываем задний фон
    scene bg living_room

    # Вводим персонажа Джека и его диалог
    show jack happy
    jack "Привет, я Джек. Рад знакомству!"

    # Вводим персонажа Эмили и ее диалог
    show emily happy
    emily "Привет, я Эмили. Тоже рада знакомству!"

    # Добавляем дополнительный диалог
    jack "Мы уже давно работаем вместе над проектом исследования бессмертия."
    emily "Да, мы оба увлечены этой темой. Надеемся, что наша работа приведет к открытию средства, которое сможет продлить жизнь людей."

    # Добавляем дополнительную реплику Джека
    jack "Кстати, я только что прочитал о новом исследовании, которое может дать нам новые знания в этой области. Хотел бы посмотреть, что это за исследование."

    # Заканчиваем сцену
    hide jack
    hide emily
    return
