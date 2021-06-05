# Home Assistant Covid 19 Malaysia
Home Assistant - Covid-19 Malaysia daily sensor based on csv from repo https://github.com/wnarifin/covid-19-malaysia

## Intro
Default Covid-19 data for Home Assistant can get from this https://www.home-assistant.io/integrations/coronavirus
But i found it only display the cumulative data. Im thinking of how to display the data daily as seen on TV.
Just found this great repo who commit daily data for Malaysia as CSV.

## Method
1.  Made the py code to read CSV and convert it to json format
2.  Extract the output json as sensor on Home Assistant configuration.yaml

## Installation
1.  Download covid.py and put in on local folder as configuration.yaml
2.  copy code from configuration.yaml to our HA.

## Thanks
