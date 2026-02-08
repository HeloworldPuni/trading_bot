//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Bollinger_RSI_Double_Strategy
// ID_model: SNOW_1Min_1BOL_bd922c70 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNOW_1Min_1BOL_bd922c70", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNOW_1Min_bd922c70(crossunder_rsi_bbupperInt, BBlower, dif_source_BBlower, dif_source_BBupper, vrsi, BBupper, crossover_rsi_bblowerInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( vrsi <= 53.708 )
		if( BBupper <= 131.645 )
			if( BBlower <= 105.33 )
				if( BBlower <= 105.162 )
					if( dif_source_BBlower <= 4.79654 )
						ret := 1.000000 // buy
					if( dif_source_BBlower > 4.79654 )
						ret := 0.625000
				if( BBlower > 105.162 )
					ret := 0.666667
			if( BBlower > 105.33 )
				if( BBupper <= 113.736 )
					if( BBupper <= 113.189 )
						if( dif_source_BBupper <= -0.39889 )
							if( BBupper <= 113.014 )
								if( BBlower <= 107.266 )
									ret := -0.285000
								if( BBlower > 107.266 )
									ret := 0.195810
							if( BBupper > 113.014 )
								if( dif_source_BBlower <= 2.2586 )
									ret := -0.310861
								if( dif_source_BBlower > 2.2586 )
									ret := 0.213333
						if( dif_source_BBupper > -0.39889 )
							if( BBlower <= 109.554 )
								ret := -0.328720
							if( BBlower > 109.554 )
								if( vrsi <= 44.0943 )
									ret := 0.346774
								if( vrsi > 44.0943 )
									ret := -0.066964
					if( BBupper > 113.189 )
						if( dif_source_BBlower <= 1.44109 )
							if( dif_source_BBupper <= -3.72954 )
								if( dif_source_BBupper <= -4.82125 )
									ret := 0.266667
								if( dif_source_BBupper > -4.82125 )
									ret := -0.512821
							if( dif_source_BBupper > -3.72954 )
								if( dif_source_BBupper <= -1.84328 )
									ret := 0.256098
								if( dif_source_BBupper > -1.84328 )
									ret := 0.611650
						if( dif_source_BBlower > 1.44109 )
							if( dif_source_BBupper <= 0.052946 )
								if( BBlower <= 111.724 )
									ret := 0.220430
								if( BBlower > 111.724 )
									ret := -0.483871
							if( dif_source_BBupper > 0.052946 )
								ret := 1.000000 // buy
				if( BBupper > 113.736 )
					if( BBlower <= 118.608 )
						if( crossunder_rsi_bbupperInt <= 0.5 )
							if( dif_source_BBlower <= 3.55009 )
								if( BBupper <= 119.575 )
									ret := -0.014628
								if( BBupper > 119.575 )
									ret := -0.231763
							if( dif_source_BBlower > 3.55009 )
								if( BBupper <= 117.987 )
									ret := 0.071090
								if( BBupper > 117.987 )
									ret := 0.414576
						if( crossunder_rsi_bbupperInt > 0.5 )
							ret := -0.117647
					if( BBlower > 118.608 )
						if( dif_source_BBlower <= 3.39956 )
							if( BBupper <= 124.757 )
								if( dif_source_BBupper <= 0.126802 )
									ret := 0.203735
								if( dif_source_BBupper > 0.126802 )
									ret := -0.482143
							if( BBupper > 124.757 )
								if( BBupper <= 128.592 )
									ret := 0.012673
								if( BBupper > 128.592 )
									ret := 0.105644
						if( dif_source_BBlower > 3.39956 )
							if( dif_source_BBlower <= 5.64624 )
								if( dif_source_BBupper <= 0.140419 )
									ret := 0.438095
								if( dif_source_BBupper > 0.140419 )
									ret := -0.806452 // sell
							if( dif_source_BBlower > 5.64624 )
								if( BBlower <= 120.294 )
									ret := 0.754386 // buy
								if( BBlower > 120.294 )
									ret := -0.219048
		if( BBupper > 131.645 )
			if( dif_source_BBlower <= 1.78415 )
				if( BBupper <= 151.488 )
					if( BBlower <= 147.999 )
						if( BBlower <= 146.338 )
							if( BBupper <= 138.587 )
								if( BBlower <= 126.53 )
									ret := -0.598684
								if( BBlower > 126.53 )
									ret := 0.033623
							if( BBupper > 138.587 )
								if( dif_source_BBupper <= -5.68056 )
									ret := 0.084806
								if( dif_source_BBupper > -5.68056 )
									ret := -0.115256
						if( BBlower > 146.338 )
							if( BBlower <= 147.723 )
								if( dif_source_BBlower <= 1.49631 )
									ret := 0.605960
								if( dif_source_BBlower > 1.49631 )
									ret := -0.240000
							if( BBlower > 147.723 )
								if( vrsi <= 49.5336 )
									ret := 0.144928
								if( vrsi > 49.5336 )
									ret := -0.600000
					if( BBlower > 147.999 )
						if( dif_source_BBupper <= -0.227935 )
							if( vrsi <= 14.8954 )
								if( BBupper <= 151.374 )
									ret := -0.630631
								if( BBupper > 151.374 )
									ret := 0.222222
							if( vrsi > 14.8954 )
								if( BBlower <= 148.091 )
									ret := -0.705882 // sell
								if( BBlower > 148.091 )
									ret := -0.314685
						if( dif_source_BBupper > -0.227935 )
							if( BBupper <= 151.074 )
								ret := -0.375000
							if( BBupper > 151.074 )
								ret := 1.000000 // buy
				if( BBupper > 151.488 )
					if( BBlower <= 163.543 )
						if( vrsi <= 1.52719 )
							if( vrsi <= 0.005423 )
								if( BBlower <= 156.963 )
									ret := 0.589744
								if( BBlower > 156.963 )
									ret := 0.132353
							if( vrsi > 0.005423 )
								if( vrsi <= 0.909086 )
									ret := 0.967742 // buy
								if( vrsi > 0.909086 )
									ret := 0.562500
						if( vrsi > 1.52719 )
							if( BBlower <= 151.154 )
								if( BBlower <= 150.253 )
									ret := 0.251969
								if( BBlower > 150.253 )
									ret := 0.605769
							if( BBlower > 151.154 )
								if( dif_source_BBupper <= -20.2378 )
									ret := 1.000000 // buy
								if( dif_source_BBupper > -20.2378 )
									ret := 0.079026
					if( BBlower > 163.543 )
						if( BBupper <= 171.773 )
							if( dif_source_BBupper <= -0.791524 )
								if( BBlower <= 164.092 )
									ret := -0.101449
								if( BBlower > 164.092 )
									ret := 0.711864 // buy
							if( dif_source_BBupper > -0.791524 )
								if( BBupper <= 165.75 )
									ret := -0.413174
								if( BBupper > 165.75 )
									ret := 0.333333
						if( BBupper > 171.773 )
							if( BBlower <= 168.003 )
								if( BBupper <= 172.791 )
									ret := 0.333333
								if( BBupper > 172.791 )
									ret := -0.428571
							if( BBlower > 168.003 )
								if( vrsi <= 38.6899 )
									ret := -0.957143 // sell
								if( vrsi > 38.6899 )
									ret := -0.600000
			if( dif_source_BBlower > 1.78415 )
				if( dif_source_BBupper <= -7.14513 )
					if( dif_source_BBupper <= -14.0993 )
						if( dif_source_BBlower <= 4.6795 )
							if( dif_source_BBlower <= 4.09108 )
								if( dif_source_BBupper <= -14.3042 )
									ret := 0.086207
								if( dif_source_BBupper > -14.3042 )
									ret := -0.894737 // sell
							if( dif_source_BBlower > 4.09108 )
								if( BBlower <= 153.807 )
									ret := -0.647059
								if( BBlower > 153.807 )
									ret := -1.000000 // sell
						if( dif_source_BBlower > 4.6795 )
							if( dif_source_BBlower <= 8.03335 )
								ret := 1.000000 // buy
							if( dif_source_BBlower > 8.03335 )
								ret := 0.625000
					if( dif_source_BBupper > -14.0993 )
						if( vrsi <= 28.5466 )
							if( dif_source_BBupper <= -8.52944 )
								if( vrsi <= 6.10841 )
									ret := 1.000000 // buy
								if( vrsi > 6.10841 )
									ret := 0.680851
							if( dif_source_BBupper > -8.52944 )
								if( dif_source_BBupper <= -7.78481 )
									ret := 0.000000
								if( dif_source_BBupper > -7.78481 )
									ret := -0.363636
						if( vrsi > 28.5466 )
							if( vrsi <= 33.476 )
								if( BBlower <= 127.996 )
									ret := 0.600000
								if( BBlower > 127.996 )
									ret := 1.000000 // buy
							if( vrsi > 33.476 )
								if( vrsi <= 37.8502 )
									ret := -0.333333
								if( vrsi > 37.8502 )
									ret := 0.675926
				if( dif_source_BBupper > -7.14513 )
					if( vrsi <= 23.1113 )
						if( dif_source_BBupper <= -3.48153 )
							if( BBlower <= 155.848 )
								if( BBupper <= 140.145 )
									ret := 0.095238
								if( BBupper > 140.145 )
									ret := 0.714286 // buy
							if( BBlower > 155.848 )
								if( dif_source_BBupper <= -4.94432 )
									ret := -0.666667
								if( dif_source_BBupper > -4.94432 )
									ret := 0.090909
						if( dif_source_BBupper > -3.48153 )
							if( BBlower <= 156.183 )
								if( dif_source_BBupper <= -2.56708 )
									ret := -0.782178 // sell
								if( dif_source_BBupper > -2.56708 )
									ret := -0.282496
							if( BBlower > 156.183 )
								if( dif_source_BBupper <= -2.8693 )
									ret := 0.838710 // buy
								if( dif_source_BBupper > -2.8693 )
									ret := -0.066298
					if( vrsi > 23.1113 )
						if( dif_source_BBlower <= 5.30043 )
							if( vrsi <= 26.0384 )
								if( BBlower <= 157.873 )
									ret := 0.042453
								if( BBlower > 157.873 )
									ret := 0.857143 // buy
							if( vrsi > 26.0384 )
								if( vrsi <= 53.1791 )
									ret := -0.084993
								if( vrsi > 53.1791 )
									ret := 0.246575
						if( dif_source_BBlower > 5.30043 )
							if( BBupper <= 138.178 )
								if( BBlower <= 123.986 )
									ret := -0.800000 // sell
								if( BBlower > 123.986 )
									ret := 0.208333
							if( BBupper > 138.178 )
								if( BBupper <= 138.693 )
									ret := -1.000000 // sell
								if( BBupper > 138.693 )
									ret := -0.369492
	if( vrsi > 53.708 )
		if( BBlower <= 111.357 )
			if( BBupper <= 122.284 )
				if( dif_source_BBupper <= -9.67905 )
					if( BBupper <= 121.258 )
						ret := 0.875000 // buy
					if( BBupper > 121.258 )
						ret := 1.000000 // buy
				if( dif_source_BBupper > -9.67905 )
					if( dif_source_BBlower <= 0.427417 )
						if( BBupper <= 110.752 )
							if( dif_source_BBlower <= 0.286116 )
								if( dif_source_BBlower <= 0.153609 )
									ret := 0.423077
								if( dif_source_BBlower > 0.153609 )
									ret := 0.745455 // buy
							if( dif_source_BBlower > 0.286116 )
								if( vrsi <= 60.782 )
									ret := -0.142857
								if( vrsi > 60.782 )
									ret := 0.456140
						if( BBupper > 110.752 )
							if( BBupper <= 111.386 )
								if( dif_source_BBlower <= 0.087732 )
									ret := 0.857143 // buy
								if( dif_source_BBlower > 0.087732 )
									ret := -0.170370
							if( BBupper > 111.386 )
								if( BBlower <= 109.852 )
									ret := -0.132075
								if( BBlower > 109.852 )
									ret := 0.356061
					if( dif_source_BBlower > 0.427417 )
						if( dif_source_BBlower <= 1.65544 )
							if( BBlower <= 109.205 )
								if( BBupper <= 112.78 )
									ret := 0.097436
								if( BBupper > 112.78 )
									ret := -0.253968
							if( BBlower > 109.205 )
								if( vrsi <= 83.9603 )
									ret := -0.018385
								if( vrsi > 83.9603 )
									ret := -0.294872
						if( dif_source_BBlower > 1.65544 )
							if( dif_source_BBupper <= 0.052005 )
								if( dif_source_BBlower <= 7.50965 )
									ret := 0.021236
								if( dif_source_BBlower > 7.50965 )
									ret := 0.691176
							if( dif_source_BBupper > 0.052005 )
								if( BBupper <= 112.846 )
									ret := 0.158798
								if( BBupper > 112.846 )
									ret := 0.439446
			if( BBupper > 122.284 )
				if( BBupper <= 123.231 )
					ret := -0.700000 // sell
				if( BBupper > 123.231 )
					if( vrsi <= 73.5476 )
						ret := -0.923077 // sell
					if( vrsi > 73.5476 )
						ret := -1.000000 // sell
		if( BBlower > 111.357 )
			if( dif_source_BBupper <= -8.09714 )
				if( vrsi <= 92.9527 )
					if( vrsi <= 89.8787 )
						if( dif_source_BBlower <= 6.16962 )
							if( BBupper <= 140.181 )
								if( dif_source_BBlower <= 3.05694 )
									ret := -0.411765
								if( dif_source_BBlower > 3.05694 )
									ret := 0.400000
							if( BBupper > 140.181 )
								if( vrsi <= 62.2727 )
									ret := 0.086957
								if( vrsi > 62.2727 )
									ret := 0.451087
						if( dif_source_BBlower > 6.16962 )
							if( BBupper <= 174.158 )
								ret := -0.857143 // sell
							if( BBupper > 174.158 )
								if( dif_source_BBlower <= 8.32397 )
									ret := 1.000000 // buy
								if( dif_source_BBlower > 8.32397 )
									ret := 0.926829 // buy
					if( vrsi > 89.8787 )
						if( BBlower <= 127.763 )
							ret := -0.875000 // sell
						if( BBlower > 127.763 )
							if( vrsi <= 91.2822 )
								ret := -0.333333
							if( vrsi > 91.2822 )
								ret := -0.500000
				if( vrsi > 92.9527 )
					if( BBlower <= 132.257 )
						ret := 0.380952
					if( BBlower > 132.257 )
						if( dif_source_BBlower <= 8.04807 )
							ret := 0.833333 // buy
						if( dif_source_BBlower > 8.04807 )
							ret := 0.900000 // buy
			if( dif_source_BBupper > -8.09714 )
				if( BBlower <= 117.809 )
					if( dif_source_BBlower <= 6.66129 )
						if( BBupper <= 117.265 )
							if( dif_source_BBlower <= 0.771338 )
								if( dif_source_BBlower <= 0.338429 )
									ret := -0.058700
								if( dif_source_BBlower > 0.338429 )
									ret := -0.308836
							if( dif_source_BBlower > 0.771338 )
								if( vrsi <= 93.8607 )
									ret := -0.172048
								if( vrsi > 93.8607 )
									ret := 0.128000
						if( BBupper > 117.265 )
							if( dif_source_BBlower <= 2.5899 )
								if( vrsi <= 57.3728 )
									ret := -0.573034
								if( vrsi > 57.3728 )
									ret := -0.132503
							if( dif_source_BBlower > 2.5899 )
								if( BBupper <= 119.986 )
									ret := 0.378190
								if( BBupper > 119.986 )
									ret := -0.013889
					if( dif_source_BBlower > 6.66129 )
						if( dif_source_BBupper <= -1.6155 )
							if( dif_source_BBlower <= 7.07363 )
								if( dif_source_BBupper <= -1.73272 )
									ret := -0.545455
								if( dif_source_BBupper > -1.73272 )
									ret := 0.166667
							if( dif_source_BBlower > 7.07363 )
								ret := -0.545455
						if( dif_source_BBupper > -1.6155 )
							if( BBupper <= 119.876 )
								ret := -1.000000 // sell
							if( BBupper > 119.876 )
								if( BBlower <= 113.14 )
									ret := -0.789474 // sell
								if( BBlower > 113.14 )
									ret := -0.111111
				if( BBlower > 117.809 )
					if( vrsi <= 96.7225 )
						if( crossover_rsi_bblowerInt <= 0.5 )
							if( dif_source_BBupper <= -2.16725 )
								if( dif_source_BBlower <= -0.870923 )
									ret := -0.816327 // sell
								if( dif_source_BBlower > -0.870923 )
									ret := 0.027582
							if( dif_source_BBupper > -2.16725 )
								if( dif_source_BBupper <= 0.562587 )
									ret := -0.057578
								if( dif_source_BBupper > 0.562587 )
									ret := -0.223181
						if( crossover_rsi_bblowerInt > 0.5 )
							if( dif_source_BBlower <= 0.125974 )
								if( vrsi <= 60.3922 )
									ret := -0.058824
								if( vrsi > 60.3922 )
									ret := -0.350000
							if( dif_source_BBlower > 0.125974 )
								if( BBlower <= 135.413 )
									ret := 0.590909
								if( BBlower > 135.413 )
									ret := -0.285714
					if( vrsi > 96.7225 )
						if( dif_source_BBlower <= 5.39854 )
							if( BBlower <= 125.724 )
								if( BBupper <= 128.103 )
									ret := 0.352617
								if( BBupper > 128.103 )
									ret := -0.254237
							if( BBlower > 125.724 )
								if( BBupper <= 130.312 )
									ret := -0.465517
								if( BBupper > 130.312 )
									ret := 0.050407
						if( dif_source_BBlower > 5.39854 )
							if( BBupper <= 131.119 )
								if( vrsi <= 98.7404 )
									ret := -0.875000 // sell
								if( vrsi > 98.7404 )
									ret := 0.080000
							if( BBupper > 131.119 )
								if( BBlower <= 128.204 )
									ret := -1.000000 // sell
								if( BBlower > 128.204 )
									ret := -0.571429
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Bollinger_RSI_Double_Strategy 
//@version=5
//strategy "Bollinger + RSI, Double Strategy (by ChartArt) v1.1", shorttitle="CA_-_RSI_Bol_Strat_1.1", overlay=true)

// ChartArt's RSI + Bollinger Bands, Double Strategy - Update
//
// Version 1.1
// Idea by ChartArt on January 18, 2015.
//
// This strategy uses the RSI indicator
// together with the Bollinger Bands
// to sell when the price is above the
// upper Bollinger Band (and to buy when
// this value is below the lower band).
//
// This simple strategy only triggers when
// both the RSI and the Bollinger Bands
// indicators are at the same time in
// a overbought or oversold condition.
//
// In this version 1.1 the strategy was
// both simplified for the user and
// made more successful in backtesting.
//
// List of my work:
// https://www.tradingview.com/u/ChartArt/
//
//  __             __  ___       __  ___
// /  ` |__|  /\  |__)  |   /\  |__)  |
// \__, |  | /~~\ |  \  |  /~~\ |  \  |
//
//

///////////// RSI
RSIlength = input.int(6, title="RSI Period Length")
RSIoverSold = 50
RSIoverBought = 50
price = close
vrsi = ta.rsi(price, RSIlength)

///////////// Bollinger Bands
BBlength = input.int(200, minval=1, title="Bollinger Period Length")
BBmult = 2 // input(2.0, minval=0.001, maxval=50,title="Bollinger Bands Standard Deviation")
BBbasis = ta.sma(price, BBlength)
BBdev = BBmult * ta.stdev(price, BBlength)
BBupper = BBbasis + BBdev
BBlower = BBbasis - BBdev
source = close
buyEntry = ta.crossover(source, BBlower)
sellEntry = ta.crossunder(source, BBupper)
plot(BBbasis, color=color.aqua, title="Bollinger Bands SMA Basis Line")
p1 = plot(BBupper, color=color.silver, title="Bollinger Bands Upper Line")
p2 = plot(BBlower, color=color.silver, title="Bollinger Bands Lower Line")
fill(p1, p2)

///////////// Colors
switch1 = input(true, title="Enable Bar Color?")
switch2 = input(true, title="Enable Background Color?")
TrendColor = (price[1] > BBupper and price < BBupper and BBbasis < BBbasis[1]) ? color.red : (price[1] < BBlower and price > BBlower and BBbasis > BBbasis[1]) ? color.green : na
// bgColor1 = color.new(TrendColor, 70)
barcolor(switch1 ? TrendColor : na)

// Using color.new() to set transparency
bgColor = color.new(TrendColor, 90)
bgcolor(switch2 ? bgColor : na)

///////////// RSI + Bollinger Bands Strategy
crossover_rsi_bblower = ta.crossover(vrsi, RSIoverSold) and ta.crossover(source, BBlower)
crossunder_rsi_bbupper = ta.crossunder(vrsi, RSIoverBought) and ta.crossunder(source, BBupper)

crossover_rsi_bblowerInt = crossover_rsi_bblower ? 1: 0    //Bool to int
crossunder_rsi_bbupperInt = crossunder_rsi_bbupper ? 1: 0  //Bool to int

dif_vrsi_RSIoverSold = vrsi - RSIoverSold
dif_source_BBlower = source - BBlower
dif_vrsi_RSIoverBought = vrsi - RSIoverBought
dif_source_BBupper = source - BBupper

// if not na(vrsi)
//     if crossover_rsi_bblower
//         strategy.entry("RSI_BB_L", strategy.long, stop=BBlower, oca_type=strategy.oca.cancel, comment="RSI_BB_L")
//     else
//         strategy.cancel(id="RSI_BB_L")
//
//     if crossunder_rsi_bbupper
//         strategy.entry("RSI_BB_S", strategy.short, stop=BBupper, oca_type=strategy.oca.cancel, comment="RSI_BB_S")
//     else
//         strategy.cancel(id="RSI_BB_S")

//plot(strategy.equity, title="equity", color=color.red, linewidth=2, style=plot.style_areabr)
// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_SNOW_1Min_bd922c70(crossunder_rsi_bbupperInt, BBlower, dif_source_BBlower, dif_source_BBupper, vrsi, BBupper, crossover_rsi_bblowerInt)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


