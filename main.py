from flask import Flask, render_template
from data import db_session
from data.movie import Movie
from data.theaters import Theater

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Главная страница
@app.route("/")
def home():
    return render_template("home.html")

# Далее страницы регионов
@app.route("/Altai_Territory")
def Altai_Territory():
    return render_template("Altai_Territory.html")


@app.route("/Amur_region")
def Amur_region():
    return render_template("Amur_region.html")


@app.route("/Astrakhan_region")
def Astrakhan_region():
    return render_template("Astrakhan_region.html")


@app.route("/Arkhangelsk_region")
def Arkhangelsk_region():
    return render_template("Arkhangelsk_region.html")


@app.route("/Belgorod_region")
def Belgorod_region():
    return render_template("Belgorod_region.html")


@app.route("/Bryansk_region")
def Bryansk_region():
    return render_template("Bryansk_region.html")


@app.route("/Vladimir_region")
def Vladimir_region():
    return render_template("Vladimir_region.html")


@app.route("/Volgograd_region")
def Volgograd_region():
    return render_template("Volgograd_region.html")


@app.route("/Vologda_region")
def Vologda_region():
    return render_template("Vologda_region.html")


@app.route("/Voronezh_region")
def Voronezh_region():
    return render_template("Voronezh_region.html")


@app.route("/Donetsk_People_s_Republic")
def Donetsk_People_s_Republic():
    return render_template("Donetsk_People_s_Republic.html")


@app.route("/Jewish_JSC")
def Jewish_JSC():
    return render_template("Jewish_JSC.html")


@app.route("/Trans_Baikal_Territory")
def Trans_Baikal_Territory():
    return render_template("Trans_Baikal_Territory.html")


@app.route("/Zaporozhye_region")
def Zaporozhye_region():
    return render_template("Zaporozhye_region.html")


@app.route("/Ivanovo_region")
def Ivanovo_region():
    return render_template("Ivanovo_region.html")


@app.route("/Irkutsk_region")
def Irkutsk_region():
    return render_template("Irkutsk_region.html")


@app.route("/Kabardino_Balkarian_Republic")
def Kabardino_Balkarian_Republic():
    return render_template("Kabardino_Balkarian_Republic.html")


@app.route("/Kaliningrad_Region")
def Kaliningrad_Region():
    return render_template("Kaliningrad_Region.html")


@app.route("/Kaluga_Region")
def Kaluga_Region():
    return render_template("Kaluga_Region.html")


@app.route("/Kamchatka_Territory")
def Kamchatka_Territory():
    return render_template("Kamchatka_Territory.html")


@app.route("/Karachay_Cherkess_Republic")
def Karachay_Cherkess_Republic():
    return render_template("Karachay_Cherkess_Republic.html")


@app.route("/Kemerovo_Region")
def Kemerovo_Region():
    return render_template("Kemerovo_Region.html")


@app.route("/Kirov_Region")
def Kirov_Region():
    return render_template("Kirov_Region.html")


@app.route("/Kostroma_Region")
def Kostroma_Region():
    return render_template("Kostroma_Region.html")


@app.route("/Krasnodarskiy_Territory")
def Krasnodarskiy_Territory():
    return render_template("Krasnodarskiy_Territory.html")


@app.route("/Krasnoyarsk_Territory")
def Krasnoyarsk_Territory():
    return render_template("Krasnoyarsk_Territory.html")


@app.route("/Kurgan_Region")
def Kurgan_Region():
    return render_template("Kurgan_Region.html")


@app.route("/Kursk_Region")
def Kursk_Region():
    return render_template("Kursk_Region.html")


@app.route("/Leningrad_Region")
def Leningrad_Region():
    return render_template("Leningrad_Region.html")


@app.route("/Lipetsk_Region")
def Lipetsk_Region():
    return render_template("Lipetsk_Region.html")


@app.route("/Luhansk_People_s_Republic")
def Luhansk_People_s_Republic():
    return render_template("Luhansk_People_s_Republic.html")


@app.route("/Magadan_Region")
def Magadan_Region():
    return render_template("Magadan_Region.html")


@app.route("/Moscow")
def Moscow():
    return render_template("Moscow.html")


@app.route("/Moscow_Region")
def Moscow_Region():
    return render_template("Moscow_Region.html")


@app.route("/Murmansk_Region")
def Murmansk_Region():
    return render_template("Murmansk_Region.html")


@app.route("/Nenets_AO")
def Nenets_AO():
    return render_template("Nenets_AO.html")


@app.route("/Nizhny_Novgorod_Region")
def Nizhny_Novgorod_Region():
    return render_template("Nizhny_Novgorod_Region.html")


@app.route("/Novgorod_Region")
def Novgorod_Region():
    return render_template("Novgorod_Region.html")


@app.route("/Novosibirsk_Region")
def Novosibirsk_Region():
    return render_template("Novosibirsk_Region.html")


@app.route("/Omsk_Region")
def Omsk_Region():
    return render_template("Omsk_Region.html")


@app.route("/Orenburg_Region")
def Orenburg_Region():
    return render_template("Orenburg_Region.html")


@app.route("/Oryol_Region")
def Oryol_Region():
    return render_template("Oryol_Region.html")


@app.route("/Penza_Region")
def Penza_Region():
    return render_template("Penza_Region.html")


@app.route("/Perm_Territory")
def Perm_Territory():
    return render_template("Perm_Territory.html")


@app.route("/Primorsky_Territory")
def Primorsky_Territory():
    return render_template("Primorsky_Territory.html")


@app.route("/Pskov_Region")
def Pskov_Region():
    return render_template("Pskov_Region.html")


@app.route("/Republic_of_Adygea")
def Republic_of_Adygea():
    return render_template("Republic_of_Adygea.html")


@app.route("/Republic_of_Altai")
def Republic_of_Altai():
    return render_template("Republic_of_Altai.html")


@app.route("/Republic_of_Bashkortostan")
def Republic_of_Bashkortostan():
    return render_template("Republic_of_Bashkortostan.html")


@app.route("/Republic_of_Buryatia")
def Republic_of_Buryatia():
    return render_template("Republic_of_Buryatia.html")


@app.route("/Republic_of_Dagestan")
def Republic_of_Dagestan():
    return render_template("Republic_of_Dagestan.html")


@app.route("/Republic_of_Ingushetia")
def Republic_of_Ingushetia():
    return render_template("Republic_of_Ingushetia.html")


@app.route("/Republic_of_Kalmykia")
def Republic_of_Kalmykia():
    return render_template("Republic_of_Kalmykia.html")


@app.route("/Republic_of_Karelia")
def Republic_of_Karelia():
    return render_template("Republic_of_Karelia.html")


@app.route("/Republic_of_Komi")
def Republic_of_Komi():
    return render_template("Republic_of_Komi.html")


@app.route("/Republic_of_Crimea")
def Republic_of_Crimea():
    return render_template("Republic_of_Crimea.html")


@app.route("/Republic_of_Mari_El")
def Republic_of_Mari_El():
    return render_template("Republic_of_Mari_El.html")


@app.route("/Republic_of_Mordovia")
def Republic_of_Mordovia():
    return render_template("Republic_of_Mordovia.html")


@app.route("/Republic_of_Sakha")
def Republic_of_Sakha():
    return render_template("Republic_of_Sakha.html")


@app.route("/Republic_of_North_Ossetia_Alania")
def Republic_of_North_Ossetia_Alania():
    return render_template("Republic_of_North_Ossetia_Alania.html")


@app.route("/Republic_of_Tatarstan")
def Republic_of_Tatarstan():
    return render_template("Republic_of_Tatarstan.html")


@app.route("/Republic_of_Tyva")
def Republic_of_Tyva():
    return render_template("Republic_of_Tyva.html")


@app.route("/Republic_of_Khakassia")
def Republic_of_Khakassia():
    return render_template("Republic_of_Khakassia.html")


@app.route("/Rostov_Region")
def Rostov_Region():
    return render_template("Rostov_Region.html")


@app.route("/Ryazan_Region")
def Ryazan_Region():
    return render_template("Ryazan_Region.html")


@app.route("/Samara_Region")
def Samara_Region():
    return render_template("Samara_Region.html")


@app.route("/Saint_Petersburg")
def Saint_Petersburg():
    return render_template("Saint_Petersburg.html")


@app.route("/Saratov_Region")
def Saratov_Region():
    return render_template("Saratov_Region.html")


@app.route("/Sakhalin_Region")
def Sakhalin_Region():
    return render_template("Sakhalin_Region.html")


@app.route("/Sverdlovsk_Region")
def Sverdlovsk_Region():
    return render_template("Sverdlovsk_Region.html")


@app.route("/Sevastopol")
def Sevastopol():
    return render_template("Sevastopol.html")


@app.route("/Smolensk_Region")
def Smolensk_Region():
    return render_template("Smolensk_Region.html")


@app.route("/Stavropol_Territory")
def Stavropol_Territory():
    return render_template("Stavropol_Territory.html")


@app.route("/Tambov_Region")
def Tambov_Region():
    return render_template("Tambov_Region.html")


@app.route("/Tver_Region")
def Tver_Region():
    return render_template("Tver_Region.html")


@app.route("/Tomsk_Region")
def Tomsk_Region():
    return render_template("Tomsk_Region.html")


@app.route("/Tula_Region")
def Tula_Region():
    return render_template("Tula_Region.html")


@app.route("/Tyumen_Region")
def Tyumen_Region():
    return render_template("Tyumen_Region.html")


@app.route("/Udmurt_Republic")
def Udmurt_Republic():
    return render_template("Udmurt_Republic.html")


@app.route("/Ulyanovsk_Region")
def Ulyanovsk_Region():
    return render_template("Ulyanovsk_Region.html")


@app.route("/Khabarovsk_Territory")
def Khabarovsk_Territory():
    return render_template("Khabarovsk_Territory.html")


@app.route("/Khanty_Mansiysk_JSC")
def Khanty_Mansiysk_JSC():
    return render_template("Khanty_Mansiysk_JSC.html")


@app.route("/Kherson_Region")
def Kherson_Region():
    return render_template("Kherson_Region.html")


@app.route("/Chelyabinsk_Region")
def Chelyabinsk_Region():
    return render_template("Chelyabinsk_Region.html")


@app.route("/Chechen_Republic")
def Chechen_Republic():
    return render_template("Chechen_Republic.html")


@app.route("/Chuvash_Republic")
def Chuvash_Republic():
    return render_template("Chuvash_Republic.html")


@app.route("/Chukotsiy_JSC")
def Chukotsiy_JSC():
    return render_template("Chukotsiy_JSC.html")


@app.route("/Yamalo_Nenets_JSC")
def Yamalo_Nenets_JSC():
    return render_template("Yamalo_Nenets_JSC.html")


@app.route("/Yaroslavl_Region")
def Yaroslavl_Region():
    return render_template("Yaroslavl_Region.html")

# Страница Театров
@app.route("/Theaters_of_the_RF")
def Theaters_of_the_RF():
    session = db_session.create_session()
    theater = session.query(Theater).all()
    return render_template("Theaters_of_the_RF.html", theater=theater)

# Страница кинотеатров
@app.route("/Cinema_RF")
def Cinema_RF():
    session = db_session.create_session()
    cinema = session.query(Movie).all()
    return render_template("Cinema_RF.html", cinema=cinema)


if __name__ == '__main__':
    db_session.global_init('db/tourism.db')
    app.run()
