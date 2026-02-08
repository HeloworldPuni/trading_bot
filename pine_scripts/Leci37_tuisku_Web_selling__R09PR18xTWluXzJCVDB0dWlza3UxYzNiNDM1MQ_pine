//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: GOOG_1Min_2BT0_1c3b4351 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_GOOG_1Min_2BT0_1c3b4351", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_GOOG_1Min_1c3b4351(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( bearPower <= -0.060705 )
		if( bbm <= 0.034997 )
			if( ema1 <= 159.503 )
				if( tema <= 159.007 )
					if( ema12 <= -0.192373 )
						if( ema13 <= -0.484596 )
							if( ema1 <= 158.849 )
								if( bullPower <= -0.429198 )
									ret := 1.000000 // buy
								if( bullPower > -0.429198 )
									ret := 0.500000
							if( ema1 > 158.849 )
								ret := -0.833333 // sell
						if( ema13 > -0.484596 )
							if( tema <= 157.031 )
								if( bearPower <= -0.231006 )
									ret := -1.000000 // sell
								if( bearPower > -0.231006 )
									ret := -0.750000 // sell
							if( tema > 157.031 )
								if( ema3 <= 158.37 )
									ret := 0.333333
								if( ema3 > 158.37 )
									ret := -0.750000 // sell
					if( ema12 > -0.192373 )
						if( ema12 <= -0.128473 )
							if( ema3 <= 158.205 )
								if( ema13 <= -0.368446 )
									ret := 0.200000
								if( ema13 > -0.368446 )
									ret := 0.842857 // buy
							if( ema3 > 158.205 )
								ret := -0.142857
						if( ema12 > -0.128473 )
							if( ema12 <= 0.007945 )
								if( ema2 <= 156.934 )
									ret := 0.345098
								if( ema2 > 156.934 )
									ret := 0.115044
							if( ema12 > 0.007945 )
								if( bullPower <= -0.065444 )
									ret := 0.909091 // buy
								if( bullPower > -0.065444 )
									ret := 0.250000
				if( tema > 159.007 )
					if( bbp <= -0.22377 )
						if( ema3 <= 159.516 )
							if( bullPower <= -0.126494 )
								ret := 0.750000 // buy
							if( bullPower > -0.126494 )
								ret := 1.000000 // buy
						if( ema3 > 159.516 )
							ret := 1.000000 // buy
					if( bbp > -0.22377 )
						if( ema3 <= 159.522 )
							if( ema13 <= -0.105796 )
								ret := 0.600000
							if( ema13 > -0.105796 )
								ret := 1.000000 // buy
						if( ema3 > 159.522 )
							ret := 0.000000
			if( ema1 > 159.503 )
				if( bullPower <= -0.237835 )
					if( ema1 <= 160.658 )
						if( ema1 <= 159.965 )
							if( ema1 <= 159.827 )
								ret := 1.000000 // buy
							if( ema1 > 159.827 )
								if( ema13 <= -0.028916 )
									ret := -0.285714
								if( ema13 > -0.028916 )
									ret := 0.833333 // buy
						if( ema1 > 159.965 )
							if( ema13 <= -0.535608 )
								ret := 0.500000
							if( ema13 > -0.535608 )
								if( tema <= 159.752 )
									ret := -0.750000 // sell
								if( tema > 159.752 )
									ret := -1.000000 // sell
					if( ema1 > 160.658 )
						if( tema <= 161.607 )
							if( bbp <= -0.585738 )
								if( ema3 <= 162.046 )
									ret := 0.972222 // buy
								if( ema3 > 162.046 )
									ret := 0.777778 // buy
							if( bbp > -0.585738 )
								ret := 0.250000
						if( tema > 161.607 )
							if( ema3 <= 185.489 )
								if( ema3 <= 178.216 )
									ret := 0.288421
								if( ema3 > 178.216 )
									ret := 0.755814 // buy
							if( ema3 > 185.489 )
								if( tema <= 186.6 )
									ret := -0.520000
								if( tema > 186.6 )
									ret := 0.409091
				if( bullPower > -0.237835 )
					if( tema <= 190.592 )
						if( ema2 <= 159.764 )
							if( bbp <= -0.248759 )
								ret := 0.166667
							if( bbp > -0.248759 )
								if( ema13 <= -0.044361 )
									ret := -1.000000 // sell
								if( ema13 > -0.044361 )
									ret := -0.200000
						if( ema2 > 159.764 )
							if( bbp <= -0.141156 )
								if( ema12 <= -0.080571 )
									ret := 0.082912
								if( ema12 > -0.080571 )
									ret := 0.200906
							if( bbp > -0.141156 )
								if( tema <= 186.374 )
									ret := -0.001748
								if( tema > 186.374 )
									ret := 0.466667
					if( tema > 190.592 )
						if( ema1 <= 190.709 )
							ret := -1.000000 // sell
						if( ema1 > 190.709 )
							if( bbm <= 0.018223 )
								if( ema13 <= -0.088272 )
									ret := -0.416667
								if( ema13 > -0.088272 )
									ret := -0.100000
							if( bbm > 0.018223 )
								if( ema12 <= -0.082307 )
									ret := 0.833333 // buy
								if( ema12 > -0.082307 )
									ret := -0.050000
		if( bbm > 0.034997 )
			if( bbm <= 1.18559 )
				if( bearPower <= -0.274601 )
					if( ema13 <= -0.579288 )
						if( ema3 <= 174.009 )
							if( ema2 <= 171.917 )
								if( bbm <= 0.194557 )
									ret := 0.177515
								if( bbm > 0.194557 )
									ret := -0.201161
							if( ema2 > 171.917 )
								if( bbm <= 0.1774 )
									ret := 0.750000 // buy
								if( bbm > 0.1774 )
									ret := -0.779412 // sell
						if( ema3 > 174.009 )
							if( ema2 <= 181.756 )
								if( bullPower <= -0.274745 )
									ret := 0.776000 // buy
								if( bullPower > -0.274745 )
									ret := 0.000000
							if( ema2 > 181.756 )
								if( ema1 <= 182.964 )
									ret := -0.973684 // sell
								if( ema1 > 182.964 )
									ret := 0.058824
					if( ema13 > -0.579288 )
						if( tema <= 153.204 )
							if( ema3 <= 150.228 )
								if( ema3 <= 149.947 )
									ret := 0.161290
								if( ema3 > 149.947 )
									ret := 0.807692 // buy
							if( ema3 > 150.228 )
								if( ema13 <= -0.312762 )
									ret := -0.698795
								if( ema13 > -0.312762 )
									ret := -0.053435
						if( tema > 153.204 )
							if( ema3 <= 167.152 )
								if( ema13 <= 0.089062 )
									ret := 0.241774
								if( ema13 > 0.089062 )
									ret := 0.730769 // buy
							if( ema3 > 167.152 )
								if( ema13 <= 0.011325 )
									ret := 0.147184
								if( ema13 > 0.011325 )
									ret := -0.180328
				if( bearPower > -0.274601 )
					if( ema1 <= 148.555 )
						ret := 1.000000 // buy
					if( ema1 > 148.555 )
						if( ema3 <= 170.513 )
							if( ema1 <= 168.468 )
								if( ema12 <= -0.056028 )
									ret := 0.001198
								if( ema12 > -0.056028 )
									ret := 0.093779
							if( ema1 > 168.468 )
								if( tema <= 168.485 )
									ret := -0.623656
								if( tema > 168.485 )
									ret := -0.127133
						if( ema3 > 170.513 )
							if( ema1 <= 170.393 )
								ret := 1.000000 // buy
							if( ema1 > 170.393 )
								if( bbm <= 0.128847 )
									ret := 0.054830
								if( bbm > 0.128847 )
									ret := 0.129659
			if( bbm > 1.18559 )
				if( bbm <= 6.22101 )
					if( ema3 <= 175.78 )
						if( tema <= 158.354 )
							ret := 0.500000
						if( tema > 158.354 )
							if( ema12 <= -0.06484 )
								if( bearPower <= -1.87861 )
									ret := -1.000000 // sell
								if( bearPower > -1.87861 )
									ret := -0.058824
							if( ema12 > -0.06484 )
								if( bearPower <= -1.30769 )
									ret := -0.250000
								if( bearPower > -1.30769 )
									ret := -0.941176 // sell
					if( ema3 > 175.78 )
						if( tema <= 183.176 )
							if( ema12 <= -0.197574 )
								if( bbp <= -1.86504 )
									ret := 0.750000 // buy
								if( bbp > -1.86504 )
									ret := 1.000000 // buy
							if( ema12 > -0.197574 )
								if( ema13 <= 0.286159 )
									ret := -0.500000
								if( ema13 > 0.286159 )
									ret := 0.777778 // buy
						if( tema > 183.176 )
							if( tema <= 189.048 )
								if( ema2 <= 186.658 )
									ret := -0.692308
								if( ema2 > 186.658 )
									ret := 0.000000
							if( tema > 189.048 )
								ret := 0.714286 // buy
				if( bbm > 6.22101 )
					if( tema <= 180.032 )
						ret := 1.000000 // buy
					if( tema > 180.032 )
						ret := 0.500000
	if( bearPower > -0.060705 )
		if( bearPower <= 0.213067 )
			if( ema1 <= 149.437 )
				if( bearPower <= -0.035662 )
					if( ema1 <= 149.238 )
						ret := -0.333333
					if( ema1 > 149.238 )
						if( ema2 <= 149.306 )
							ret := 0.750000 // buy
						if( ema2 > 149.306 )
							ret := 1.000000 // buy
				if( bearPower > -0.035662 )
					if( ema12 <= 0.147758 )
						if( ema12 <= -0.016853 )
							if( bearPower <= 0.027234 )
								ret := 1.000000 // buy
							if( bearPower > 0.027234 )
								ret := 0.500000
						if( ema12 > -0.016853 )
							if( bullPower <= 0.320719 )
								ret := 1.000000 // buy
							if( bullPower > 0.320719 )
								ret := 0.714286 // buy
					if( ema12 > 0.147758 )
						ret := 0.200000
			if( ema1 > 149.437 )
				if( ema3 <= 177.225 )
					if( ema3 <= 177.133 )
						if( ema12 <= 0.06011 )
							if( bearPower <= 0.059164 )
								if( ema13 <= -0.160008 )
									ret := -0.181230
								if( ema13 > -0.160008 )
									ret := 0.038737
							if( bearPower > 0.059164 )
								if( ema3 <= 159.048 )
									ret := -0.258893
								if( ema3 > 159.048 )
									ret := -0.070029
						if( ema12 > 0.06011 )
							if( ema3 <= 164.745 )
								if( ema2 <= 161.709 )
									ret := 0.050929
								if( ema2 > 161.709 )
									ret := 0.213028
							if( ema3 > 164.745 )
								if( bbp <= 0.038623 )
									ret := -0.388889
								if( bbp > 0.038623 )
									ret := 0.045336
					if( ema3 > 177.133 )
						if( bullPower <= 0.058104 )
							if( tema <= 177.317 )
								if( ema1 <= 177.132 )
									ret := 0.250000
								if( ema1 > 177.132 )
									ret := 0.000000
							if( tema > 177.317 )
								ret := -0.500000
						if( bullPower > 0.058104 )
							if( bbp <= 0.37241 )
								if( ema13 <= -0.011391 )
									ret := 0.100000
								if( ema13 > -0.011391 )
									ret := 0.638889
							if( bbp > 0.37241 )
								if( bullPower <= 0.273389 )
									ret := -0.222222
								if( bullPower > 0.273389 )
									ret := 0.600000
				if( ema3 > 177.225 )
					if( bbp <= 0.131677 )
						if( ema3 <= 180.875 )
							if( ema12 <= -0.032788 )
								if( ema1 <= 177.754 )
									ret := -0.481928
								if( ema1 > 177.754 )
									ret := -0.068376
							if( ema12 > -0.032788 )
								if( ema1 <= 177.815 )
									ret := 0.125581
								if( ema1 > 177.815 )
									ret := -0.046448
						if( ema3 > 180.875 )
							if( ema2 <= 183.634 )
								if( ema3 <= 183.456 )
									ret := 0.175879
								if( ema3 > 183.456 )
									ret := 0.578947
							if( ema2 > 183.634 )
								if( ema2 <= 192.712 )
									ret := 0.055693
								if( ema2 > 192.712 )
									ret := -0.409091
					if( bbp > 0.131677 )
						if( ema12 <= -0.007928 )
							if( ema13 <= -0.127174 )
								if( ema13 <= -0.159057 )
									ret := -0.346154
								if( ema13 > -0.159057 )
									ret := 0.500000
							if( ema13 > -0.127174 )
								if( bearPower <= 0.045079 )
									ret := -0.296875
								if( bearPower > 0.045079 )
									ret := -0.730159 // sell
						if( ema12 > -0.007928 )
							if( ema3 <= 177.415 )
								if( bearPower <= 0.057028 )
									ret := -0.623656
								if( bearPower > 0.057028 )
									ret := -0.160377
							if( ema3 > 177.415 )
								if( ema12 <= 0.247145 )
									ret := -0.067396
								if( ema12 > 0.247145 )
									ret := 0.303030
		if( bearPower > 0.213067 )
			if( ema13 <= 0.384072 )
				if( tema <= 174.518 )
					if( ema3 <= 149.477 )
						if( ema13 <= 0.117763 )
							ret := 0.000000
						if( ema13 > 0.117763 )
							if( bbm <= 0.140414 )
								ret := -1.000000 // sell
							if( bbm > 0.140414 )
								ret := -0.750000 // sell
					if( ema3 > 149.477 )
						if( tema <= 150.057 )
							if( ema3 <= 149.567 )
								ret := 0.750000 // buy
							if( ema3 > 149.567 )
								ret := 1.000000 // buy
						if( tema > 150.057 )
							if( ema2 <= 174.085 )
								if( tema <= 160.945 )
									ret := -0.269521
								if( tema > 160.945 )
									ret := -0.120453
							if( ema2 > 174.085 )
								ret := 1.000000 // buy
				if( tema > 174.518 )
					if( ema12 <= 0.221523 )
						if( bearPower <= 0.425829 )
							if( bbm <= 0.145776 )
								if( ema3 <= 177.107 )
									ret := -0.525253
								if( ema3 > 177.107 )
									ret := -0.263158
							if( bbm > 0.145776 )
								if( ema13 <= 0.233667 )
									ret := 0.305085
								if( ema13 > 0.233667 )
									ret := -0.259740
						if( bearPower > 0.425829 )
							if( ema2 <= 185.993 )
								if( ema2 <= 178.526 )
									ret := -0.842105 // sell
								if( ema2 > 178.526 )
									ret := 0.000000
							if( ema2 > 185.993 )
								ret := -1.000000 // sell
					if( ema12 > 0.221523 )
						if( ema3 <= 177.724 )
							if( bbm <= 0.148692 )
								ret := -1.000000 // sell
							if( bbm > 0.148692 )
								if( bearPower <= 0.27969 )
									ret := -1.000000 // sell
								if( bearPower > 0.27969 )
									ret := -0.565217
						if( ema3 > 177.724 )
							if( bbm <= 0.155884 )
								if( ema13 <= 0.362016 )
									ret := -0.454545
								if( ema13 > 0.362016 )
									ret := 0.833333 // buy
							if( bbm > 0.155884 )
								if( bbm <= 0.378794 )
									ret := -0.894737 // sell
								if( bbm > 0.378794 )
									ret := 0.250000
			if( ema13 > 0.384072 )
				if( tema <= 158.099 )
					if( bbm <= 0.095514 )
						if( ema12 <= 0.196943 )
							ret := -0.750000 // sell
						if( ema12 > 0.196943 )
							if( bbm <= 0.054961 )
								if( ema13 <= 0.816086 )
									ret := 0.111111
								if( ema13 > 0.816086 )
									ret := -0.400000
							if( bbm > 0.054961 )
								ret := 0.750000 // buy
					if( bbm > 0.095514 )
						if( ema13 <= 0.603379 )
							if( ema12 <= 0.247191 )
								if( tema <= 154.268 )
									ret := -0.750000 // sell
								if( tema > 154.268 )
									ret := -0.375000
							if( ema12 > 0.247191 )
								if( tema <= 151.84 )
									ret := -0.250000
								if( tema > 151.84 )
									ret := -1.000000 // sell
						if( ema13 > 0.603379 )
							if( ema2 <= 155.272 )
								if( ema3 <= 153.274 )
									ret := -0.500000
								if( ema3 > 153.274 )
									ret := -1.000000 // sell
							if( ema2 > 155.272 )
								ret := 0.333333
				if( tema > 158.099 )
					if( ema3 <= 163.113 )
						if( bullPower <= 1.21447 )
							if( tema <= 163.722 )
								if( ema12 <= 0.27713 )
									ret := 0.330508
								if( ema12 > 0.27713 )
									ret := -0.154930
							if( tema > 163.722 )
								if( ema3 <= 163.01 )
									ret := 1.000000 // buy
								if( ema3 > 163.01 )
									ret := 0.500000
						if( bullPower > 1.21447 )
							if( ema2 <= 161.866 )
								if( ema2 <= 158.858 )
									ret := 0.545455
								if( ema2 > 158.858 )
									ret := 0.924528 // buy
							if( ema2 > 161.866 )
								if( ema1 <= 163.126 )
									ret := -1.000000 // sell
								if( ema1 > 163.126 )
									ret := 0.100000
					if( ema3 > 163.113 )
						if( bearPower <= 0.363838 )
							if( ema3 <= 167.292 )
								if( ema13 <= 0.477455 )
									ret := 0.208333
								if( ema13 > 0.477455 )
									ret := -0.364583
							if( ema3 > 167.292 )
								if( ema1 <= 169.048 )
									ret := 0.902439 // buy
								if( ema1 > 169.048 )
									ret := 0.110112
						if( bearPower > 0.363838 )
							if( ema1 <= 178.163 )
								if( tema <= 177.748 )
									ret := -0.283333
								if( tema > 177.748 )
									ret := -0.714286 // sell
							if( ema1 > 178.163 )
								if( ema3 <= 178.621 )
									ret := 0.791667 // buy
								if( ema3 > 178.621 )
									ret := 0.062857
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0


//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


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
float op_operation = decision_tree_0_GOOG_1Min_1c3b4351(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)

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


