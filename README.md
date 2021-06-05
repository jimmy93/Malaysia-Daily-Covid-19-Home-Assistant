# Home Assistant Covid 19 Malaysia
Home Assistant - Covid-19 Malaysia daily sensor based on csv from repo https://github.com/wnarifin/covid-19-malaysia

## Intro
Default Covid-19 data for Home Assistant can get from this https://www.home-assistant.io/integrations/coronavirus
But i found it only display the cumulative data. Im thinking of how to display the data daily as seen on TV.
Just found this great repo who commit daily data for Malaysia as CSV.

## How It Work
1.  Made the py code to read CSV (read the last row) and convert it to json format
2.  Extract the output json as sensor on Home Assistant configuration.yaml

## How To Setup
1.  Download [covid.py](covid.py) and put in on local folder as configuration.yaml
2.  copy code from [configuration.yaml](configuration.yaml) to our HA.

### Sensor create from configuration.yaml
1.  covid_kes_baharu
2.  covid_kes_mati
3.  covid_jumlah_kes
4.  covid_jumlah_kes_mati
5.  covid_kes_sembuh
6.  covid_jumlah_kes_sembuh
7.  covid_icu
8.  covid_support

## Thanks
Thanks to @wnarifin
FB: Ajimm Al
my fav community
Home Assistant Malaysia https://www.facebook.com/groups/homeassistantmalaysia
Kelab DIY Smart Home https://www.facebook.com/groups/694589921358327
Telegram Group: Smart Home Malaysia https://t.me/smart_home_malaysia
