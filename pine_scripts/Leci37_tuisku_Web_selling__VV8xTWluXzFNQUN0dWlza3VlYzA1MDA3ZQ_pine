//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: U_1Min_1MAC_ec05007e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_1MAC_ec05007e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_ec05007e(histB_IsUpInt, macd_IsBelowInt, macd, histB_IsDownInt, macd_IsAboveInt, histA_IsDownInt, histA_IsUpInt, hist, signal)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7,max_features=sqrt, min_samples_leaf=4,random_state=843828734)
	if( histA_IsUpInt <= 0.5 )
		if( macd <= -0.084698 )
			if( histB_IsUpInt <= 0.5 )
				if( signal <= -0.061402 )
					if( macd <= -0.102081 )
						if( macd_IsBelowInt <= 0.5 )
							if( macd <= -0.124552 )
								ret := 0.404255
							if( macd > -0.124552 )
								ret := 0.781250 // buy
						if( macd_IsBelowInt > 0.5 )
							if( signal <= -0.08573 )
								ret := 0.458599
							if( signal > -0.08573 )
								ret := -0.675000
					if( macd > -0.102081 )
						if( signal <= -0.079332 )
							if( hist <= -0.00688 )
								ret := -0.893617 // sell
							if( hist > -0.00688 )
								ret := -0.215278
						if( signal > -0.079332 )
							if( hist <= -0.029448 )
								ret := -1.000000 // sell
							if( hist > -0.029448 )
								ret := 0.189655
				if( signal > -0.061402 )
					if( signal <= -0.004578 )
						if( signal <= -0.052141 )
							if( macd <= -0.091852 )
								ret := 0.600000
							if( macd > -0.091852 )
								ret := 0.925926 // buy
						if( signal > -0.052141 )
							if( hist <= -0.081076 )
								ret := 0.954545 // buy
							if( hist > -0.081076 )
								ret := 0.274725
					if( signal > -0.004578 )
						ret := -1.000000 // sell
			if( histB_IsUpInt > 0.5 )
				if( signal <= -0.098715 )
					if( signal <= -0.116563 )
						if( signal <= -0.242401 )
							if( hist <= -0.052123 )
								ret := 0.800000 // buy
							if( hist > -0.052123 )
								ret := -0.260870
						if( signal > -0.242401 )
							if( signal <= -0.162855 )
								ret := 0.839286 // buy
							if( signal > -0.162855 )
								ret := 0.458333
					if( signal > -0.116563 )
						if( hist <= -0.006223 )
							if( hist <= -0.008984 )
								ret := -0.367647
							if( hist > -0.008984 )
								ret := -0.888889 // sell
						if( hist > -0.006223 )
							if( macd <= -0.111342 )
								ret := -0.272727
							if( macd > -0.111342 )
								ret := 0.538462
				if( signal > -0.098715 )
					if( hist <= -0.043859 )
						if( signal <= -0.048201 )
							if( macd <= -0.110958 )
								ret := -0.411111
							if( macd > -0.110958 )
								ret := 0.230769
						if( signal > -0.048201 )
							if( signal <= -0.031586 )
								ret := 0.785714 // buy
							if( signal > -0.031586 )
								ret := -0.285714
					if( hist > -0.043859 )
						if( signal <= -0.068033 )
							if( hist <= -0.002619 )
								ret := 0.616393
							if( hist > -0.002619 )
								ret := 0.830189 // buy
						if( signal > -0.068033 )
							if( macd <= -0.08971 )
								ret := 0.153846
							if( macd > -0.08971 )
								ret := 0.888889 // buy
		if( macd > -0.084698 )
			if( signal <= -0.065461 )
				if( macd_IsAboveInt <= 0.5 )
					if( hist <= -0.010619 )
						if( macd <= -0.082327 )
							if( histB_IsUpInt <= 0.5 )
								ret := 0.411765
							if( histB_IsUpInt > 0.5 )
								ret := 0.857143 // buy
						if( macd > -0.082327 )
							if( histB_IsDownInt <= 0.5 )
								ret := -0.333333
							if( histB_IsDownInt > 0.5 )
								ret := -0.857143 // sell
					if( hist > -0.010619 )
						if( signal <= -0.079445 )
							if( histB_IsUpInt <= 0.5 )
								ret := 1.000000 // buy
							if( histB_IsUpInt > 0.5 )
								ret := -0.324324
						if( signal > -0.079445 )
							if( macd <= -0.076785 )
								ret := -0.891304 // sell
							if( macd > -0.076785 )
								ret := -0.323529
				if( macd_IsAboveInt > 0.5 )
					if( macd <= -0.071263 )
						if( macd <= -0.079624 )
							if( hist <= 0.029061 )
								ret := -0.087719
							if( hist > 0.029061 )
								ret := -1.000000 // sell
						if( macd > -0.079624 )
							if( hist <= 0.008711 )
								ret := 0.783784 // buy
							if( hist > 0.008711 )
								ret := 0.057692
					if( macd > -0.071263 )
						if( signal <= -0.085187 )
							if( hist <= 0.091256 )
								ret := 0.255319
							if( hist > 0.091256 )
								ret := -1.000000 // sell
						if( signal > -0.085187 )
							if( macd <= -0.066934 )
								ret := -0.857143 // sell
							if( macd > -0.066934 )
								ret := -0.209091
			if( signal > -0.065461 )
				if( histB_IsUpInt <= 0.5 )
					if( macd <= -0.050432 )
						if( macd_IsAboveInt <= 0.5 )
							if( hist <= -0.046028 )
								ret := -0.590164
							if( hist > -0.046028 )
								ret := -0.085714
						if( macd_IsAboveInt > 0.5 )
							if( signal <= -0.060312 )
								ret := -0.636364
							if( signal > -0.060312 )
								ret := 0.020408
					if( macd > -0.050432 )
						if( signal <= -0.049508 )
							if( hist <= 0.004456 )
								ret := 0.914894 // buy
							if( hist > 0.004456 )
								ret := 0.377301
						if( signal > -0.049508 )
							if( macd_IsBelowInt <= 0.5 )
								ret := 0.030034
							if( macd_IsBelowInt > 0.5 )
								ret := 0.072793
				if( histB_IsUpInt > 0.5 )
					if( hist <= -0.000572 )
						if( signal <= -0.043561 )
							if( signal <= -0.057982 )
								ret := 0.424893
							if( signal > -0.057982 )
								ret := 0.177353
						if( signal > -0.043561 )
							if( hist <= -0.039367 )
								ret := -0.283505
							if( hist > -0.039367 )
								ret := -0.037170
					if( hist > -0.000572 )
						if( hist <= -0.000427 )
							if( signal <= 0.02587 )
								ret := -0.312102
							if( signal > 0.02587 )
								ret := -0.931034 // sell
						if( hist > -0.000427 )
							if( macd <= -0.001935 )
								ret := -0.181651
							if( macd > -0.001935 )
								ret := 0.030369
	if( histA_IsUpInt > 0.5 )
		if( macd <= 0.035454 )
			if( signal <= -0.041983 )
				if( signal <= -0.068808 )
					if( hist <= 0.025007 )
						if( signal <= -0.0773 )
							if( signal <= -0.141773 )
								ret := -0.439655
							if( signal > -0.141773 )
								ret := 0.096367
						if( signal > -0.0773 )
							if( macd <= -0.063995 )
								ret := -0.740741 // sell
							if( macd > -0.063995 )
								ret := -0.217822
					if( hist > 0.025007 )
						if( macd <= -0.052655 )
							if( hist <= 0.026713 )
								ret := -0.916667 // sell
							if( hist > 0.026713 )
								ret := -0.103723
						if( macd > -0.052655 )
							if( signal <= -0.10738 )
								ret := -1.000000 // sell
							if( signal > -0.10738 )
								ret := -0.615894
				if( signal > -0.068808 )
					if( signal <= -0.065743 )
						if( macd <= -0.019678 )
							if( macd <= -0.065475 )
								ret := 0.111111
							if( macd > -0.065475 )
								ret := 0.802198 // buy
						if( macd > -0.019678 )
							ret := -0.333333
					if( signal > -0.065743 )
						if( signal <= -0.045312 )
							if( signal <= -0.050664 )
								ret := 0.108889
							if( signal > -0.050664 )
								ret := -0.136247
						if( signal > -0.045312 )
							if( hist <= 0.005257 )
								ret := 0.715909 // buy
							if( hist > 0.005257 )
								ret := 0.154122
			if( signal > -0.041983 )
				if( signal <= -0.037769 )
					if( signal <= -0.038611 )
						if( hist <= 0.006929 )
							if( hist <= 0.000844 )
								ret := 0.250000
							if( hist > 0.000844 )
								ret := -0.496454
						if( hist > 0.006929 )
							if( signal <= -0.038748 )
								ret := -0.223256
							if( signal > -0.038748 )
								ret := 0.777778 // buy
					if( signal > -0.038611 )
						if( macd <= -0.026597 )
							if( macd <= -0.032907 )
								ret := -0.768293 // sell
							if( macd > -0.032907 )
								ret := -0.918919 // sell
						if( macd > -0.026597 )
							if( hist <= 0.024121 )
								ret := -0.214286
							if( hist > 0.024121 )
								ret := 1.000000 // buy
				if( signal > -0.037769 )
					if( signal <= -0.034162 )
						if( hist <= 0.019844 )
							if( signal <= -0.035176 )
								ret := 0.101852
							if( signal > -0.035176 )
								ret := 0.373832
						if( hist > 0.019844 )
							if( signal <= -0.037253 )
								ret := 1.000000 // buy
							if( signal > -0.037253 )
								ret := 0.688525
					if( signal > -0.034162 )
						if( signal <= -0.024073 )
							if( signal <= -0.025514 )
								ret := -0.159649
							if( signal > -0.025514 )
								ret := -0.379679
						if( signal > -0.024073 )
							if( macd <= -0.003459 )
								ret := -0.006078
							if( macd > -0.003459 )
								ret := -0.138821
		if( macd > 0.035454 )
			if( signal <= 0.107243 )
				if( signal <= 0.073669 )
					if( macd <= 0.05258 )
						if( macd <= 0.041485 )
							if( signal <= 0.030564 )
								ret := 0.207547
							if( signal > 0.030564 )
								ret := -0.375661
						if( macd > 0.041485 )
							if( signal <= 0.025371 )
								ret := 0.604520
							if( signal > 0.025371 )
								ret := 0.131846
					if( macd > 0.05258 )
						if( signal <= 0.002948 )
							if( hist <= 0.062107 )
								ret := -0.600000
							if( hist > 0.062107 )
								ret := -1.000000 // sell
						if( signal > 0.002948 )
							if( hist <= 0.008321 )
								ret := -0.326271
							if( hist > 0.008321 )
								ret := 0.031532
				if( signal > 0.073669 )
					if( hist <= 0.014565 )
						if( hist <= 0.002662 )
							if( macd <= 0.077737 )
								ret := 0.800000 // buy
							if( macd > 0.077737 )
								ret := -0.142857
						if( hist > 0.002662 )
							if( signal <= 0.07607 )
								ret := 1.000000 // buy
							if( signal > 0.07607 )
								ret := 0.714286 // buy
					if( hist > 0.014565 )
						if( signal <= 0.101496 )
							if( macd <= 0.113688 )
								ret := -0.125000
							if( macd > 0.113688 )
								ret := 0.630435
						if( signal > 0.101496 )
							ret := -1.000000 // sell
			if( signal > 0.107243 )
				if( macd <= 0.264434 )
					if( macd <= 0.171555 )
						if( hist <= 0.017245 )
							if( signal <= 0.116639 )
								ret := -0.562500
							if( signal > 0.116639 )
								ret := -0.916667 // sell
						if( hist > 0.017245 )
							if( hist <= 0.022029 )
								ret := 0.444444
							if( hist > 0.022029 )
								ret := -0.444444
					if( macd > 0.171555 )
						ret := -1.000000 // sell
				if( macd > 0.264434 )
					if( signal <= 0.203169 )
						ret := 1.000000 // buy
					if( signal > 0.203169 )
						ret := 0.333333
	
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
float op_operation = decision_tree_0_U_1Min_ec05007e(histB_IsUpInt, macd_IsBelowInt, macd, histB_IsDownInt, macd_IsAboveInt, histA_IsDownInt, histA_IsUpInt, hist, signal)

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


