//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: SHOP_1Min_1MAC_e744b75e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SHOP_1Min_1MAC_e744b75e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SHOP_1Min_e744b75e(signal, histA_IsDownInt, macd, hist, histA_IsUpInt, histB_IsDownInt, histB_IsUpInt, macd_IsBelowInt, macd_IsAboveInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( histB_IsDownInt <= 0.5 )
		if( histA_IsUpInt <= 0.5 )
			if( hist <= 0.001066 )
				if( macd <= -0.301431 )
					if( macd <= -0.357679 )
						if( macd <= -0.640774 )
							if( hist <= -1.7452 )
								ret := -0.500000
							if( hist > -1.7452 )
								if( hist <= -1.28177 )
									ret := 0.500000
								if( hist > -1.28177 )
									ret := 0.952381 // buy
						if( macd > -0.640774 )
							if( macd <= -0.416999 )
								if( hist <= -0.037362 )
									ret := -0.730769 // sell
								if( hist > -0.037362 )
									ret := -0.363636
							if( macd > -0.416999 )
								if( macd <= -0.403178 )
									ret := 1.000000 // buy
								if( macd > -0.403178 )
									ret := 0.100000
					if( macd > -0.357679 )
						if( signal <= -0.324841 )
							ret := 0.500000
						if( signal > -0.324841 )
							if( macd <= -0.354237 )
								ret := 1.000000 // buy
							if( macd > -0.354237 )
								if( macd <= -0.352061 )
									ret := 0.500000
								if( macd > -0.352061 )
									ret := 0.887324 // buy
				if( macd > -0.301431 )
					if( hist <= -0.04827 )
						if( hist <= -0.149259 )
							if( macd <= 0.710168 )
								if( signal <= 0.309776 )
									ret := 0.200000
								if( signal > 0.309776 )
									ret := 0.952381 // buy
							if( macd > 0.710168 )
								if( hist <= -0.252683 )
									ret := 0.600000
								if( hist > -0.252683 )
									ret := -0.500000
						if( hist > -0.149259 )
							if( hist <= -0.052495 )
								if( macd <= -0.27816 )
									ret := -0.875000 // sell
								if( macd > -0.27816 )
									ret := 0.093333
							if( hist > -0.052495 )
								if( macd <= -0.072781 )
									ret := 0.081301
								if( macd > -0.072781 )
									ret := 0.423729
					if( hist > -0.04827 )
						if( histB_IsUpInt <= 0.5 )
							if( macd <= 0.108944 )
								if( signal <= -0.188422 )
									ret := -1.000000 // sell
								if( signal > -0.188422 )
									ret := 0.054896
							if( macd > 0.108944 )
								if( hist <= 0.000266 )
									ret := 0.200000
								if( hist > 0.000266 )
									ret := -0.722222 // sell
						if( histB_IsUpInt > 0.5 )
							if( signal <= -0.049751 )
								if( signal <= -0.08391 )
									ret := -0.010882
								if( signal > -0.08391 )
									ret := 0.134809
							if( signal > -0.049751 )
								if( signal <= 0.272369 )
									ret := -0.027993
								if( signal > 0.272369 )
									ret := -0.555556
			if( hist > 0.001066 )
				if( signal <= -0.11093 )
					if( hist <= 0.493034 )
						if( signal <= -0.128221 )
							if( macd <= -0.677772 )
								ret := 1.000000 // buy
							if( macd > -0.677772 )
								if( hist <= 0.087016 )
									ret := 0.067797
								if( hist > 0.087016 )
									ret := -0.440000
						if( signal > -0.128221 )
							if( macd <= -0.105724 )
								if( signal <= -0.11446 )
									ret := -0.615385
								if( signal > -0.11446 )
									ret := 0.000000
							if( macd > -0.105724 )
								if( hist <= 0.022456 )
									ret := 0.000000
								if( hist > 0.022456 )
									ret := -0.366667
					if( hist > 0.493034 )
						ret := -1.000000 // sell
				if( signal > -0.11093 )
					if( signal <= -0.05897 )
						if( hist <= 0.064171 )
							if( macd <= -0.053785 )
								if( macd <= -0.065314 )
									ret := 0.228330
								if( macd > -0.065314 )
									ret := 0.608997
							if( macd > -0.053785 )
								if( macd <= -0.048839 )
									ret := -0.067308
								if( macd > -0.048839 )
									ret := 0.273756
						if( hist > 0.064171 )
							if( signal <= -0.065109 )
								if( signal <= -0.103717 )
									ret := 0.166667
								if( signal > -0.103717 )
									ret := -0.651163
							if( signal > -0.065109 )
								if( macd <= 0.022445 )
									ret := -0.500000
								if( macd > 0.022445 )
									ret := 0.666667
					if( signal > -0.05897 )
						if( hist <= 0.003474 )
							if( macd <= 0.011012 )
								if( hist <= 0.002579 )
									ret := 0.092243
								if( hist > 0.002579 )
									ret := -0.069565
							if( macd > 0.011012 )
								if( hist <= 0.001089 )
									ret := 0.900000 // buy
								if( hist > 0.001089 )
									ret := 0.283370
						if( hist > 0.003474 )
							if( macd <= 1.02816 )
								if( macd <= 0.264471 )
									ret := 0.073100
								if( macd > 0.264471 )
									ret := -0.183432
							if( macd > 1.02816 )
								ret := 1.000000 // buy
		if( histA_IsUpInt > 0.5 )
			if( hist <= 0.020789 )
				if( macd <= 0.136777 )
					if( macd <= 0.103003 )
						if( macd <= -0.063507 )
							if( signal <= -0.145166 )
								if( signal <= -0.170099 )
									ret := 0.112727
								if( signal > -0.170099 )
									ret := -0.276596
							if( signal > -0.145166 )
								if( hist <= 0.003824 )
									ret := 0.285124
								if( hist > 0.003824 )
									ret := 0.134807
						if( macd > -0.063507 )
							if( signal <= -0.04303 )
								if( signal <= -0.053649 )
									ret := -0.056063
								if( signal > -0.053649 )
									ret := -0.226624
							if( signal > -0.04303 )
								if( signal <= 0.030283 )
									ret := 0.034957
								if( signal > 0.030283 )
									ret := -0.041962
					if( macd > 0.103003 )
						if( macd <= 0.111632 )
							if( hist <= 0.015889 )
								if( signal <= 0.099991 )
									ret := 0.107143
								if( signal > 0.099991 )
									ret := 0.666667
							if( hist > 0.015889 )
								if( hist <= 0.018813 )
									ret := 1.000000 // buy
								if( hist > 0.018813 )
									ret := 0.555556
						if( macd > 0.111632 )
							if( macd <= 0.122235 )
								if( signal <= 0.095141 )
									ret := 1.000000 // buy
								if( signal > 0.095141 )
									ret := -0.229885
							if( macd > 0.122235 )
								if( hist <= 0.010708 )
									ret := 0.714286 // buy
								if( hist > 0.010708 )
									ret := 0.060000
				if( macd > 0.136777 )
					if( signal <= 0.149607 )
						if( signal <= 0.141378 )
							if( signal <= 0.13398 )
								if( hist <= 0.010734 )
									ret := -1.000000 // sell
								if( hist > 0.010734 )
									ret := -0.266667
							if( signal > 0.13398 )
								if( macd <= 0.145254 )
									ret := 0.500000
								if( macd > 0.145254 )
									ret := -0.166667
						if( signal > 0.141378 )
							if( signal <= 0.144832 )
								if( macd <= 0.158564 )
									ret := -0.750000 // sell
								if( macd > 0.158564 )
									ret := -1.000000 // sell
							if( signal > 0.144832 )
								ret := -0.500000
					if( signal > 0.149607 )
						if( macd <= 0.177365 )
							if( signal <= 0.162767 )
								if( hist <= 0.018668 )
									ret := 0.200000
								if( hist > 0.018668 )
									ret := -0.600000
							if( signal > 0.162767 )
								if( macd <= 0.170823 )
									ret := -1.000000 // sell
								if( macd > 0.170823 )
									ret := -0.555556
						if( macd > 0.177365 )
							if( macd <= 0.19336 )
								if( macd <= 0.186954 )
									ret := 0.454545
								if( macd > 0.186954 )
									ret := 1.000000 // buy
							if( macd > 0.19336 )
								if( signal <= 0.196979 )
									ret := -0.727273 // sell
								if( signal > 0.196979 )
									ret := -0.029412
			if( hist > 0.020789 )
				if( macd <= -0.037958 )
					if( macd <= -0.109178 )
						if( signal <= -0.179198 )
							if( signal <= -0.389435 )
								if( signal <= -0.53635 )
									ret := -0.114286
								if( signal > -0.53635 )
									ret := 0.584615
							if( signal > -0.389435 )
								if( hist <= 0.042033 )
									ret := 0.095238
								if( hist > 0.042033 )
									ret := -0.130435
						if( signal > -0.179198 )
							if( hist <= 0.039988 )
								if( signal <= -0.137921 )
									ret := -0.422680
								if( signal > -0.137921 )
									ret := 0.600000
							if( hist > 0.039988 )
								if( hist <= 0.044054 )
									ret := 0.533333
								if( hist > 0.044054 )
									ret := -0.372093
					if( macd > -0.109178 )
						if( hist <= 0.073317 )
							if( signal <= -0.090828 )
								if( hist <= 0.064316 )
									ret := 0.161290
								if( hist > 0.064316 )
									ret := 0.568627
							if( signal > -0.090828 )
								if( signal <= -0.074126 )
									ret := -0.180392
								if( signal > -0.074126 )
									ret := 0.297297
						if( hist > 0.073317 )
							if( macd <= -0.104508 )
								ret := 0.500000
							if( macd > -0.104508 )
								if( signal <= -0.187217 )
									ret := -1.000000 // sell
								if( signal > -0.187217 )
									ret := -0.408163
				if( macd > -0.037958 )
					if( signal <= -0.111763 )
						ret := -1.000000 // sell
					if( signal > -0.111763 )
						if( macd <= 0.005604 )
							if( hist <= 0.072609 )
								if( hist <= 0.062469 )
									ret := -0.146266
								if( hist > 0.062469 )
									ret := -0.591837
							if( hist > 0.072609 )
								if( signal <= -0.085937 )
									ret := 0.000000
								if( signal > -0.085937 )
									ret := 0.900000 // buy
						if( macd > 0.005604 )
							if( signal <= 0.040775 )
								if( signal <= -0.061293 )
									ret := -0.547619
								if( signal > -0.061293 )
									ret := 0.014446
							if( signal > 0.040775 )
								if( hist <= 0.153821 )
									ret := -0.147258
								if( hist > 0.153821 )
									ret := 0.301587
	if( histB_IsDownInt > 0.5 )
		if( signal <= -0.251096 )
			if( signal <= -0.27376 )
				if( hist <= -0.026646 )
					if( macd <= -0.359488 )
						if( signal <= -0.356207 )
							ret := 1.000000 // buy
						if( signal > -0.356207 )
							ret := 0.666667
					if( macd > -0.359488 )
						ret := 0.250000
				if( hist > -0.026646 )
					ret := -0.400000
			if( signal > -0.27376 )
				if( hist <= -0.053048 )
					ret := 1.000000 // buy
				if( hist > -0.053048 )
					if( macd <= -0.276901 )
						ret := -1.000000 // sell
					if( macd > -0.276901 )
						ret := 1.000000 // buy
		if( signal > -0.251096 )
			if( signal <= -0.092037 )
				if( hist <= -0.002885 )
					if( hist <= -0.124287 )
						if( macd <= -0.510024 )
							ret := 1.000000 // buy
						if( macd > -0.510024 )
							if( hist <= -0.169244 )
								if( hist <= -0.179293 )
									ret := -0.625000
								if( hist > -0.179293 )
									ret := 0.000000
							if( hist > -0.169244 )
								if( signal <= -0.173869 )
									ret := -0.500000
								if( signal > -0.173869 )
									ret := -0.952381 // sell
					if( hist > -0.124287 )
						if( macd <= -0.155007 )
							if( hist <= -0.02943 )
								if( hist <= -0.07798 )
									ret := 0.375000
								if( hist > -0.07798 )
									ret := -0.051546
							if( hist > -0.02943 )
								if( signal <= -0.193102 )
									ret := -0.160000
								if( signal > -0.193102 )
									ret := 0.439560
						if( macd > -0.155007 )
							if( signal <= -0.096982 )
								if( signal <= -0.142077 )
									ret := -0.888889 // sell
								if( signal > -0.142077 )
									ret := -0.022654
							if( signal > -0.096982 )
								if( signal <= -0.095963 )
									ret := -0.875000 // sell
								if( signal > -0.095963 )
									ret := -0.350000
				if( hist > -0.002885 )
					if( signal <= -0.122724 )
						if( hist <= -0.002282 )
							if( macd <= -0.153402 )
								ret := 0.000000
							if( macd > -0.153402 )
								if( hist <= -0.002482 )
									ret := -0.500000
								if( hist > -0.002482 )
									ret := -0.800000 // sell
						if( hist > -0.002282 )
							if( signal <= -0.140373 )
								if( macd <= -0.146672 )
									ret := -1.000000 // sell
								if( macd > -0.146672 )
									ret := -0.250000
							if( signal > -0.140373 )
								ret := -1.000000 // sell
					if( signal > -0.122724 )
						if( signal <= -0.102352 )
							ret := -0.166667
						if( signal > -0.102352 )
							ret := -0.500000
			if( signal > -0.092037 )
				if( signal <= -0.049813 )
					if( macd <= -0.170127 )
						if( hist <= -0.095737 )
							if( signal <= -0.083905 )
								if( macd <= -0.204515 )
									ret := -0.500000
								if( macd > -0.204515 )
									ret := 0.500000
							if( signal > -0.083905 )
								if( macd <= -0.185311 )
									ret := -0.611111
								if( macd > -0.185311 )
									ret := -0.947368 // sell
						if( hist > -0.095737 )
							ret := 0.400000
					if( macd > -0.170127 )
						if( macd <= -0.054845 )
							if( macd <= -0.15186 )
								if( hist <= -0.112322 )
									ret := 0.250000
								if( hist > -0.112322 )
									ret := 0.800000 // buy
							if( macd > -0.15186 )
								if( macd <= -0.135598 )
									ret := -0.452381
								if( macd > -0.135598 )
									ret := 0.234624
						if( macd > -0.054845 )
							if( hist <= -0.001758 )
								if( macd <= -0.05422 )
									ret := 0.800000 // buy
								if( macd > -0.05422 )
									ret := 1.000000 // buy
							if( hist > -0.001758 )
								if( macd <= -0.051909 )
									ret := 0.687500
								if( macd > -0.051909 )
									ret := 0.000000
				if( signal > -0.049813 )
					if( signal <= 0.030615 )
						if( signal <= 0.010314 )
							if( hist <= -0.137195 )
								if( macd <= -0.242278 )
									ret := 0.000000
								if( macd > -0.242278 )
									ret := 0.875000 // buy
							if( hist > -0.137195 )
								if( macd <= 0.007789 )
									ret := 0.096999
								if( macd > 0.007789 )
									ret := 0.711111 // buy
						if( signal > 0.010314 )
							if( hist <= -0.080087 )
								if( macd <= -0.071376 )
									ret := 0.142857
								if( macd > -0.071376 )
									ret := 0.888889 // buy
							if( hist > -0.080087 )
								if( macd <= -0.026004 )
									ret := -0.340000
								if( macd > -0.026004 )
									ret := 0.030457
					if( signal > 0.030615 )
						if( macd <= 0.01717 )
							if( hist <= -0.046224 )
								if( hist <= -0.052368 )
									ret := 0.326471
								if( hist > -0.052368 )
									ret := -0.492063
							if( hist > -0.046224 )
								if( signal <= 0.034848 )
									ret := 0.166667
								if( signal > 0.034848 )
									ret := 0.512000
						if( macd > 0.01717 )
							if( hist <= -0.114588 )
								if( signal <= 0.646848 )
									ret := 0.761905 // buy
								if( signal > 0.646848 )
									ret := -0.166667
							if( hist > -0.114588 )
								if( signal <= 0.456759 )
									ret := 0.110662
								if( signal > 0.456759 )
									ret := -0.500000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator MACD_ULT_MTF 
//@version=5
//indicator title="CM_MacD_Ult_MTF", shorttitle="CM_Ult_MacD_MTF", overlay=false)

source = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input.timeframe(title="Use Different Timeframe? Uncheck Box Above", defval="60")
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")

res = useCurrentRes ? timeframe.period : resCustom

fastLength = input.int(12, minval=1)
slowLength = input.int(26, minval=1)
signalLength = input.int(9, minval=1)

fastMA = ta.ema(source, fastLength)
slowMA = ta.ema(source, slowLength)

macd = fastMA - slowMA
signal = ta.sma(macd, signalLength)
hist = macd - signal

outMacD = request.security(syminfo.tickerid, res, macd)
outSignal = request.security(syminfo.tickerid, res, signal)
outHist = request.security(syminfo.tickerid, res, hist)

histA_IsUp = outHist > outHist[1] and outHist > 0
histA_IsDown = outHist < outHist[1] and outHist > 0
histB_IsDown = outHist < outHist[1] and outHist <= 0
histB_IsUp = outHist > outHist[1] and outHist <= 0

// MacD Color Definitions
macd_IsAbove = outMacD >= outSignal
macd_IsBelow = outMacD < outSignal

plot_color = hist_colorChange ? histA_IsUp ? color.aqua : histA_IsDown ? color.blue : histB_IsDown ? color.red : histB_IsUp ? color.maroon : color.yellow : color.gray
macd_color = macd_colorChange ? macd_IsAbove ? color.lime : color.red : color.red
signal_color = macd_colorChange ? macd_IsAbove ? color.yellow : color.yellow : color.lime

circleYPosition = outSignal

plot(smd and outMacD ? outMacD : na, title="MACD", color=macd_color, linewidth=4)
plot(smd and outSignal ? outSignal : na, title="Signal Line", color=signal_color, style=plot.style_line, linewidth=2)
plot(sh and outHist ? outHist : na, title="Histogram", color=plot_color, style=plot.style_histogram, linewidth=4)
plot(sd and ta.cross(outMacD, outSignal) ? circleYPosition : na, title="Cross", style=plot.style_circles, linewidth=4, color=macd_color)
hline(0, '0 Line', linestyle=hline.style_solid, linewidth=2, color=color.white)

histA_IsUpInt = histA_IsUp ? 1: 0
histA_IsDownInt = histA_IsDown ? 1: 0
histB_IsDownInt = histB_IsDown ? 1: 0
histB_IsUpInt = histB_IsUp ? 1: 0
macd_IsAboveInt = macd_IsAbove ? 1: 0
macd_IsBelowInt = macd_IsBelow ? 1: 0

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
float op_operation = decision_tree_0_SHOP_1Min_e744b75e(signal, histA_IsDownInt, macd, hist, histA_IsUpInt, histB_IsDownInt, histB_IsUpInt, macd_IsBelowInt, macd_IsAboveInt)

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


