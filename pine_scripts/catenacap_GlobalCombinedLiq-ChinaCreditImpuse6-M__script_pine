//@version=5
indicator("Global Liquidity", overlay=true, scale=scale.left)

// Input params
currency = input.string('USD', "Currency")
resolution = input.timeframe('W', "Resolution", options=[ 'D', 'W', 'M' ])
global_fill_display = input.bool(true, "Display Global liquidity fill area?")
global_line_display = input.bool(true, "Display Global liquidity line?")

// Central bank balances
bor = request.security('RUCBBS', resolution, close, currency=currency) // Russia
rbi = request.security('INCBBS', resolution, close, currency=currency) // India
snb = request.security('CHCBBS', resolution, close, currency=currency) // Switzerland
boe = request.security('GBBBS', resolution, close, currency=currency) // England
pboc = request.security('CNCBBS', resolution, close, currency=currency) // China
boj = request.security('JPCBBS', resolution, close, currency=currency) // Japan
ecb = request.security('EUCBBS', resolution, close, currency=currency) // Europe
fed = request.security('USCBBS', resolution, close, currency=currency) // US

// Combine smaller CBs, BoE, PBoC, BoJ, ECB, and FED into one line
combined_liquidity = bor + rbi + snb + boe + pboc + boj + ecb + fed

// China Credit Impulse Index (6 Months Forward) data
// Source: https://en.macromicro.me/charts/46664/cn-bloomberg-credit-impulse-6m-forward [DevTools/Network/FetchXHR/stat/response]
float china_credit_impulse = na
t = time

china_credit_impulse := t == timestamp("2008-03-01") ? 21.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-04-01") ? 20.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-05-01") ? 20.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-06-01") ? 20.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-07-01") ? 20.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-08-01") ? 21.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-09-01") ? 21.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-10-01") ? 20.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-11-01") ? 21.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2008-12-01") ? 20.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-01-01") ? 20.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-02-01") ? 19.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-03-01") ? 19.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-04-01") ? 18.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-05-01") ? 19.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-06-01") ? 20.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-07-01") ? 21.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-08-01") ? 24.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-09-01") ? 29.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-10-01") ? 28.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-11-01") ? 31.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2009-12-01") ? 36.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-01-01") ? 36.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-02-01") ? 37.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-03-01") ? 39.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-04-01") ? 39.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-05-01") ? 41.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-06-01") ? 40.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-07-01") ? 40.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-08-01") ? 40.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-09-01") ? 38.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-10-01") ? 38.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-11-01") ? 37.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2010-12-01") ? 34.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-01-01") ? 33.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-02-01") ? 34.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-03-01") ? 33.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-04-01") ? 33.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-05-01") ? 33.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-06-01") ? 34.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-07-01") ? 32.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-08-01") ? 31.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-09-01") ? 31.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-10-01") ? 30.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-11-01") ? 30.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2011-12-01") ? 30.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-01-01") ? 28.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-02-01") ? 28.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-03-01") ? 27.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-04-01") ? 25.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-05-01") ? 25.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-06-01") ? 25.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-07-01") ? 23.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-08-01") ? 24.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-09-01") ? 24.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-10-01") ? 23.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-11-01") ? 23.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2012-12-01") ? 24.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-01-01") ? 25.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-02-01") ? 25.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-03-01") ? 27.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-04-01") ? 28.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-05-01") ? 28.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-06-01") ? 29.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-07-01") ? 31.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-08-01") ? 31.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-09-01") ? 32.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-10-01") ? 33.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-11-01") ? 33.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2013-12-01") ? 32.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-01-01") ? 31.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-02-01") ? 32.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-03-01") ? 31.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-04-01") ? 30.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-05-01") ? 30.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-06-01") ? 29.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-07-01") ? 29.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-08-01") ? 28.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-09-01") ? 28.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-10-01") ? 27.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-11-01") ? 27.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2014-12-01") ? 28.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-01-01") ? 27.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-02-01") ? 26.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-03-01") ? 26.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-04-01") ? 25.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-05-01") ? 25.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-06-01") ? 25.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-07-01") ? 24.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-08-01") ? 25.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-09-01") ? 23.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-10-01") ? 22.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-11-01") ? 22.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2015-12-01") ? 23.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-01-01") ? 24.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-02-01") ? 24.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-03-01") ? 26.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-04-01") ? 25.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-05-01") ? 26.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-06-01") ? 27.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-07-01") ? 28.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-08-01") ? 28.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-09-01") ? 30.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-10-01") ? 31.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-11-01") ? 31.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2016-12-01") ? 31.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-01-01") ? 30.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-02-01") ? 31.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-03-01") ? 31.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-04-01") ? 30.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-05-01") ? 31.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-06-01") ? 31.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-07-01") ? 30.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-08-01") ? 31.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-09-01") ? 30.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-10-01") ? 29.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-11-01") ? 29.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2017-12-01") ? 29.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-01-01") ? 30.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-02-01") ? 29.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-03-01") ? 29.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-04-01") ? 29.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-05-01") ? 29.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-06-01") ? 28.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-07-01") ? 27.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-08-01") ? 27.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-09-01") ? 26.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-10-01") ? 25.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-11-01") ? 24.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2018-12-01") ? 24.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-01-01") ? 23.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-02-01") ? 23.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-03-01") ? 23.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-04-01") ? 22.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-05-01") ? 21.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-06-01") ? 21.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-07-01") ? 22.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-08-01") ? 22.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-09-01") ? 24.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-10-01") ? 23.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-11-01") ? 23.7 : china_credit_impulse
china_credit_impulse := t == timestamp("2019-12-01") ? 24.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-01-01") ? 23.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-02-01") ? 23.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-03-01") ? 23.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-04-01") ? 22.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-05-01") ? 23.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-06-01") ? 23.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-07-01") ? 23.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-08-01") ? 23.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-09-01") ? 26.2 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-10-01") ? 27.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-11-01") ? 29.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2020-12-01") ? 29.8 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-01-01") ? 29.9 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-02-01") ? 31.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-03-01") ? 32.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-04-01") ? 32.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-05-01") ? 32.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-06-01") ? 31.5 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-07-01") ? 30.3 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-08-01") ? 31.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-09-01") ? 29.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-10-01") ? 27.0 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-11-01") ? 25.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2021-12-01") ? 25.79 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-01-01") ? 24.61 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-02-01") ? 24.1 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-03-01") ? 23.6 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-04-01") ? 23.21 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-05-01") ? 23.64 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-06-01") ? 24.4 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-07-01") ? 24.76 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-08-01") ? 24.26 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-09-01") ? 25.94 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-10-01") ? 24.41 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-11-01") ? 25.26 : china_credit_impulse
china_credit_impulse := t == timestamp("2022-12-01") ? 26.75 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-01-01") ? 25.92 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-02-01") ? 25.57 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-03-01") ? 26.36 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-04-01") ? 25.48 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-05-01") ? 25.09 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-06-01") ? 24.28 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-07-01") ? 24.53 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-08-01") ? 26.16 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-09-01") ? 26.54 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-10-01") ? 26.17 : china_credit_impulse
china_credit_impulse := t == timestamp("2023-11-01") ? 25.24 : china_credit_impulse



plot(global_fill_display ? combined_liquidity : na, color=color.new(color.blue, 50), style=plot.style_area, linewidth=0)
plot(global_line_display ? combined_liquidity : na, color=color.new(color.blue, 100), linewidth=2)
plot(china_credit_impulse, color=color.new(color.red, 100), linewidth=2)

hline(0, "Zero", color=color.gray, linestyle=hline.style_dotted)
