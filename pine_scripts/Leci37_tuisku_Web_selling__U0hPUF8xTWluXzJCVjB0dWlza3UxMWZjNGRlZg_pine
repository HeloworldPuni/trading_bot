//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Vortex_Indicator
// ID_model: SHOP_1Min_2BV0_11fc4def Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SHOP_1Min_2BV0_11fc4def", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SHOP_1Min_11fc4def(bbm, bearPower, bbp, bullPower, BBPower_Color, VIP_VIM, VIM, VIP)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=0.7, min_samples_leaf=7,min_samples_split=10, random_state=843828734)
	if( bullPower <= -0.038622 )
		if( bbm <= 0.004 )
			if( bearPower <= -0.096745 )
				if( VIP <= 1.19431 )
					if( VIP <= 0.921434 )
						if( bearPower <= -0.176564 )
							if( bbp <= -0.589462 )
								ret := 0.416667
							if( bbp > -0.589462 )
								if( bbp <= -0.397569 )
									ret := 1.000000 // buy
								if( bbp > -0.397569 )
									ret := 0.750000 // buy
						if( bearPower > -0.176564 )
							if( VIP <= 0.836574 )
								ret := 0.062500
							if( VIP > 0.836574 )
								ret := 0.555556
					if( VIP > 0.921434 )
						if( VIM <= 1.60589 )
							if( VIP <= 1.15554 )
								if( VIP_VIM <= -0.269401 )
									ret := 0.777778 // buy
								if( VIP_VIM > -0.269401 )
									ret := 1.000000 // buy
							if( VIP > 1.15554 )
								ret := -0.125000
						if( VIM > 1.60589 )
							if( VIP_VIM <= -1.3526 )
								ret := -0.937500 // sell
							if( VIP_VIM > -1.3526 )
								if( VIM <= 1.88634 )
									ret := -0.545455
								if( VIM > 1.88634 )
									ret := 0.083333
				if( VIP > 1.19431 )
					if( VIP_VIM <= 1.09952 )
						if( VIP <= 1.84739 )
							if( VIP_VIM <= 0.044866 )
								if( VIM <= 1.79634 )
									ret := 0.343750
								if( VIM > 1.79634 )
									ret := 0.806452 // buy
							if( VIP_VIM > 0.044866 )
								if( bullPower <= -0.158183 )
									ret := 1.000000 // buy
								if( bullPower > -0.158183 )
									ret := 0.714286 // buy
						if( VIP > 1.84739 )
							if( VIM <= 5.50899 )
								if( VIM <= 3.39104 )
									ret := 0.552632
								if( VIM > 3.39104 )
									ret := 0.293839
							if( VIM > 5.50899 )
								if( VIP_VIM <= 0.066093 )
									ret := 0.670139
								if( VIP_VIM > 0.066093 )
									ret := 0.342857
					if( VIP_VIM > 1.09952 )
						if( VIP <= 20.4538 )
							ret := -0.687500
						if( VIP > 20.4538 )
							ret := 0.583333
			if( bearPower > -0.096745 )
				if( VIP <= 8.642 )
					if( VIM <= 1.98941 )
						if( VIM <= 1.64451 )
							if( VIM <= 1.00084 )
								ret := -0.384615
							if( VIM > 1.00084 )
								if( bbp <= -0.084327 )
									ret := 0.235955
								if( bbp > -0.084327 )
									ret := 0.600000
						if( VIM > 1.64451 )
							if( VIP_VIM <= 0.162018 )
								if( VIP_VIM <= -0.178659 )
									ret := -0.362500
								if( VIP_VIM > -0.178659 )
									ret := 0.782609 // buy
							if( VIP_VIM > 0.162018 )
								if( VIP_VIM <= 0.332809 )
									ret := -0.913043 // sell
								if( VIP_VIM > 0.332809 )
									ret := -0.387097
					if( VIM > 1.98941 )
						if( VIM <= 5.85439 )
							if( VIM <= 5.43385 )
								if( VIP_VIM <= -0.467409 )
									ret := 0.178808
								if( VIP_VIM > -0.467409 )
									ret := 0.377778
							if( VIM > 5.43385 )
								if( VIP_VIM <= -0.324028 )
									ret := 0.500000
								if( VIP_VIM > -0.324028 )
									ret := 0.961538 // buy
						if( VIM > 5.85439 )
							if( VIP <= 5.80308 )
								if( VIP_VIM <= -0.593559 )
									ret := 0.217391
								if( VIP_VIM > -0.593559 )
									ret := -0.826087 // sell
							if( VIP > 5.80308 )
								if( VIP <= 6.41714 )
									ret := 0.750000 // buy
								if( VIP > 6.41714 )
									ret := -0.028571
				if( VIP > 8.642 )
					if( VIP_VIM <= -2.35 )
						ret := -0.500000
					if( VIP_VIM > -2.35 )
						if( VIP_VIM <= -0.015198 )
							if( VIP <= 36.9316 )
								if( VIM <= 29.6133 )
									ret := 0.797297 // buy
								if( VIM > 29.6133 )
									ret := 0.300000
							if( VIP > 36.9316 )
								ret := 1.000000 // buy
						if( VIP_VIM > -0.015198 )
							if( VIM <= 19.0353 )
								if( VIP <= 12.1958 )
									ret := 0.772727 // buy
								if( VIP > 12.1958 )
									ret := -0.400000
							if( VIM > 19.0353 )
								if( bearPower <= -0.069331 )
									ret := 0.836735 // buy
								if( bearPower > -0.069331 )
									ret := 0.468085
		if( bbm > 0.004 )
			if( bbm <= 0.383373 )
				if( VIP <= 0.88517 )
					if( bbp <= -0.546744 )
						if( bbm <= 0.274165 )
							if( VIP_VIM <= -0.971513 )
								if( bullPower <= -0.496113 )
									ret := -0.500000
								if( bullPower > -0.496113 )
									ret := 0.511111
							if( VIP_VIM > -0.971513 )
								if( bearPower <= -0.543938 )
									ret := -0.560748
								if( bearPower > -0.543938 )
									ret := -0.199336
						if( bbm > 0.274165 )
							if( VIP <= 0.766432 )
								if( VIM <= 1.44731 )
									ret := 0.829268 // buy
								if( VIM > 1.44731 )
									ret := -0.388889
							if( VIP > 0.766432 )
								if( bbp <= -0.560512 )
									ret := -0.192982
								if( bbp > -0.560512 )
									ret := -1.000000 // sell
					if( bbp > -0.546744 )
						if( bearPower <= -0.326921 )
							if( bearPower <= -0.377309 )
								if( VIP <= 0.707148 )
									ret := 0.800000 // buy
								if( VIP > 0.707148 )
									ret := -0.697674
							if( bearPower > -0.377309 )
								if( VIP <= 0.828453 )
									ret := 0.315000
								if( VIP > 0.828453 )
									ret := 0.828571 // buy
						if( bearPower > -0.326921 )
							if( VIP <= 0.540648 )
								if( VIP <= 0.526693 )
									ret := 0.186916
								if( VIP > 0.526693 )
									ret := 0.660000
							if( VIP > 0.540648 )
								if( VIP <= 0.577414 )
									ret := -0.318408
								if( VIP > 0.577414 )
									ret := 0.038787
				if( VIP > 0.88517 )
					if( VIM <= 0.929799 )
						if( VIP_VIM <= 0.244663 )
							if( VIM <= 0.900133 )
								ret := 1.000000 // buy
							if( VIM > 0.900133 )
								ret := 0.916667 // buy
						if( VIP_VIM > 0.244663 )
							ret := 0.500000
					if( VIM > 0.929799 )
						if( VIP_VIM <= 0.500757 )
							if( bbp <= -0.332374 )
								if( VIP <= 1.36384 )
									ret := 0.160187
								if( VIP > 1.36384 )
									ret := 0.485714
							if( bbp > -0.332374 )
								if( bbm <= 0.006071 )
									ret := -0.440000
								if( bbm > 0.006071 )
									ret := 0.106015
						if( VIP_VIM > 0.500757 )
							if( bullPower <= -0.113039 )
								if( VIP <= 4.48393 )
									ret := -0.954545 // sell
								if( VIP > 4.48393 )
									ret := -0.476190
							if( bullPower > -0.113039 )
								if( bearPower <= -0.127932 )
									ret := 0.833333 // buy
								if( bearPower > -0.127932 )
									ret := -0.238095
			if( bbm > 0.383373 )
				if( VIP <= 0.955878 )
					if( VIP <= 0.63789 )
						if( VIM <= 1.51802 )
							if( VIM <= 1.46758 )
								ret := 0.272727
							if( VIM > 1.46758 )
								ret := -0.600000
						if( VIM > 1.51802 )
							if( bullPower <= -4.5804 )
								ret := 1.000000 // buy
							if( bullPower > -4.5804 )
								ret := 0.400000
					if( VIP > 0.63789 )
						if( bearPower <= -0.546637 )
							if( bullPower <= -0.141215 )
								if( bbp <= -1.13683 )
									ret := 0.965517 // buy
								if( bbp > -1.13683 )
									ret := 1.000000 // buy
							if( bullPower > -0.141215 )
								if( VIP_VIM <= -0.328511 )
									ret := 0.625000
								if( VIP_VIM > -0.328511 )
									ret := 1.000000 // buy
						if( bearPower > -0.546637 )
							ret := 0.565217
				if( VIP > 0.955878 )
					if( bullPower <= -0.201547 )
						if( VIP <= 1.07176 )
							ret := -0.636364
						if( VIP > 1.07176 )
							ret := -1.000000 // sell
					if( bullPower > -0.201547 )
						if( VIM <= 1.47896 )
							ret := 0.909091 // buy
						if( VIM > 1.47896 )
							ret := -0.095238
	if( bullPower > -0.038622 )
		if( bbp <= 0.378985 )
			if( VIP <= 21.2112 )
				if( bbm <= 0.003558 )
					if( bearPower <= 0.050833 )
						if( bbp <= 0.031702 )
							if( bearPower <= 0.014204 )
								if( VIM <= 1.76565 )
									ret := -0.072761
								if( VIM > 1.76565 )
									ret := 0.096005
							if( bearPower > 0.014204 )
								if( VIP <= 4.8407 )
									ret := 0.218182
								if( VIP > 4.8407 )
									ret := 0.611111
						if( bbp > 0.031702 )
							if( VIP_VIM <= -0.443227 )
								if( bbm <= 3e-06 )
									ret := -0.135659
								if( bbm > 3e-06 )
									ret := -0.857143 // sell
							if( VIP_VIM > -0.443227 )
								if( VIM <= 2.49705 )
									ret := -0.106796
								if( VIM > 2.49705 )
									ret := 0.093023
					if( bearPower > 0.050833 )
						if( VIP <= 1.86982 )
							if( VIP <= 1.22518 )
								if( VIM <= 1.06189 )
									ret := -0.368421
								if( VIM > 1.06189 )
									ret := -0.852941 // sell
							if( VIP > 1.22518 )
								if( VIM <= 1.32194 )
									ret := -0.202797
								if( VIM > 1.32194 )
									ret := -0.507317
						if( VIP > 1.86982 )
							if( VIM <= 19.6758 )
								if( VIP_VIM <= 1.60696 )
									ret := -0.142077
								if( VIP_VIM > 1.60696 )
									ret := 0.436620
							if( VIM > 19.6758 )
								if( VIP <= 20.4483 )
									ret := -1.000000 // sell
								if( VIP > 20.4483 )
									ret := -0.833333 // sell
				if( bbm > 0.003558 )
					if( bbp <= -0.502785 )
						if( bullPower <= 0.23019 )
							if( bbm <= 0.603342 )
								ret := 0.448276
							if( bbm > 0.603342 )
								if( bbp <= -0.904726 )
									ret := 0.800000 // buy
								if( bbp > -0.904726 )
									ret := 1.000000 // buy
						if( bullPower > 0.23019 )
							ret := -0.250000
					if( bbp > -0.502785 )
						if( VIP <= 0.879563 )
							if( bullPower <= 0.015807 )
								if( VIM <= 1.14503 )
									ret := -0.082776
								if( VIM > 1.14503 )
									ret := 0.047738
							if( bullPower > 0.015807 )
								if( bbp <= -0.040501 )
									ret := -0.298107
								if( bbp > -0.040501 )
									ret := 0.037678
						if( VIP > 0.879563 )
							if( VIP <= 1.63647 )
								if( VIP <= 1.34014 )
									ret := 0.046669
								if( VIP > 1.34014 )
									ret := 0.146897
							if( VIP > 1.63647 )
								if( bbp <= 0.103389 )
									ret := 0.047408
								if( bbp > 0.103389 )
									ret := -0.136802
			if( VIP > 21.2112 )
				if( VIM <= 71.6939 )
					if( VIP_VIM <= 1.61137 )
						if( bullPower <= 0.076469 )
							if( VIP <= 22.788 )
								if( BBPower_Color <= 0.5 )
									ret := 1.000000 // buy
								if( BBPower_Color > 0.5 )
									ret := 0.500000
							if( VIP > 22.788 )
								if( VIP <= 36.7533 )
									ret := 0.290909
								if( VIP > 36.7533 )
									ret := 0.633929
						if( bullPower > 0.076469 )
							if( bbp <= 0.164356 )
								ret := -0.700000 // sell
							if( bbp > 0.164356 )
								if( VIP_VIM <= 1.28295 )
									ret := 0.446602
								if( VIP_VIM > 1.28295 )
									ret := -0.200000
					if( VIP_VIM > 1.61137 )
						if( VIM <= 48.7387 )
							if( VIM <= 40.8699 )
								if( VIM <= 26.4717 )
									ret := -0.142857
								if( VIM > 26.4717 )
									ret := 0.320000
							if( VIM > 40.8699 )
								ret := -0.789474 // sell
						if( VIM > 48.7387 )
							if( VIM <= 55.855 )
								ret := 0.583333
							if( VIM > 55.855 )
								if( VIP <= 67.82 )
									ret := 0.153846
								if( VIP > 67.82 )
									ret := 0.222222
				if( VIM > 71.6939 )
					if( bbp <= 0.212246 )
						if( VIP_VIM <= 0.290053 )
							if( VIP_VIM <= -1.80509 )
								if( VIP_VIM <= -2.93501 )
									ret := 0.428571
								if( VIP_VIM > -2.93501 )
									ret := 0.545455
							if( VIP_VIM > -1.80509 )
								if( bearPower <= 0.064903 )
									ret := -0.541667
								if( bearPower > 0.064903 )
									ret := 0.600000
						if( VIP_VIM > 0.290053 )
							if( VIM <= 349.748 )
								if( bearPower <= 0.032797 )
									ret := 0.478261
								if( bearPower > 0.032797 )
									ret := 0.944444 // buy
							if( VIM > 349.748 )
								ret := -0.166667
					if( bbp > 0.212246 )
						if( bearPower <= 0.141778 )
							ret := -0.692308
						if( bearPower > 0.141778 )
							ret := -0.933333 // sell
		if( bbp > 0.378985 )
			if( bearPower <= 1.0218 )
				if( VIP_VIM <= 0.839915 )
					if( VIP_VIM <= 0.630804 )
						if( bbp <= 0.996235 )
							if( VIM <= 0.813753 )
								if( VIP_VIM <= 0.50185 )
									ret := 0.277174
								if( VIP_VIM > 0.50185 )
									ret := -0.166667
							if( VIM > 0.813753 )
								if( VIP_VIM <= -0.215307 )
									ret := 0.190909
								if( VIP_VIM > -0.215307 )
									ret := -0.274247
						if( bbp > 0.996235 )
							if( VIP_VIM <= 0.528509 )
								if( bbm <= 0.382624 )
									ret := -0.545455
								if( bbm > 0.382624 )
									ret := -0.875000 // sell
							if( VIP_VIM > 0.528509 )
								ret := 0.266667
					if( VIP_VIM > 0.630804 )
						if( VIP <= 1.67578 )
							if( VIM <= 0.621992 )
								if( bullPower <= 0.373821 )
									ret := -0.410714
								if( bullPower > 0.373821 )
									ret := 0.303030
							if( VIM > 0.621992 )
								if( bbp <= 0.409556 )
									ret := -0.164179
								if( bbp > 0.409556 )
									ret := -0.585284
						if( VIP > 1.67578 )
							if( VIP_VIM <= 0.757732 )
								if( bullPower <= 0.425588 )
									ret := -0.660000
								if( bullPower > 0.425588 )
									ret := 0.115385
							if( VIP_VIM > 0.757732 )
								if( VIP_VIM <= 0.834085 )
									ret := 0.410714
								if( VIP_VIM > 0.834085 )
									ret := -0.846154 // sell
				if( VIP_VIM > 0.839915 )
					if( VIP <= 4.88049 )
						if( bbm <= 0.094248 )
							if( VIM <= 3.33424 )
								if( VIP_VIM <= 1.71078 )
									ret := 0.146067
								if( VIP_VIM > 1.71078 )
									ret := 0.642857
							if( VIM > 3.33424 )
								if( bearPower <= 0.207726 )
									ret := 1.000000 // buy
								if( bearPower > 0.207726 )
									ret := 0.571429
						if( bbm > 0.094248 )
							if( bbm <= 0.222302 )
								if( bbp <= 0.730542 )
									ret := -0.020833
								if( bbp > 0.730542 )
									ret := -0.520000
							if( bbm > 0.222302 )
								if( bearPower <= 0.631384 )
									ret := 0.614286
								if( bearPower > 0.631384 )
									ret := -0.928571 // sell
					if( VIP > 4.88049 )
						if( VIM <= 19.8706 )
							if( bbp <= 0.405039 )
								ret := 0.181818
							if( bbp > 0.405039 )
								if( VIP <= 14.0032 )
									ret := -0.522388
								if( VIP > 14.0032 )
									ret := -0.956522 // sell
						if( VIM > 19.8706 )
							if( VIP <= 39.7833 )
								ret := 1.000000 // buy
							if( VIP > 39.7833 )
								if( bbp <= 0.667714 )
									ret := 0.000000
								if( bbp > 0.667714 )
									ret := -0.642857
			if( bearPower > 1.0218 )
				if( bullPower <= 2.48227 )
					if( bbm <= 0.650081 )
						if( VIP <= 2.21026 )
							ret := 1.000000 // buy
						if( VIP > 2.21026 )
							ret := 0.461538
					if( bbm > 0.650081 )
						ret := -0.818182 // sell
				if( bullPower > 2.48227 )
					ret := 1.000000 // buy
	
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


//CODE associated with the technical indicator L_Vortex_Indicator 
//@version=5
//indicator title = "Vortex Indicator", shorttitle="VI", format=format.price, precision=4, timeframe="", timeframe_gaps=true)
period_ = input.int(14, title="Length", minval=2)
VMP = math.sum( math.abs( high - low[1]), period_ )
VMM = math.sum( math.abs( low - high[1]), period_ )
STR = math.sum( ta.atr(1), period_ )
VIP = VMP / STR
VIM = VMM / STR

VIP_VIM = VIP - VIM

plot(VIP, title="VI +", color=#2962FF)
plot(VIM, title="VI -", color=#E91E63)
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
float op_operation = decision_tree_0_SHOP_1Min_11fc4def(bbm, bearPower, bbp, bullPower, BBPower_Color, VIP_VIM, VIM, VIP)

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


