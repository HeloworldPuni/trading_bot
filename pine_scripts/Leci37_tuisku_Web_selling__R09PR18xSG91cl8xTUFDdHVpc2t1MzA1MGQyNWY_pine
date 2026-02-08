//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: GOOG_1Hour_1MAC_3050d25f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_GOOG_1Hour_1MAC_3050d25f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_GOOG_1Hour_3050d25f(macd, macd_IsBelowInt, signal, histB_IsUpInt, macd_IsAboveInt, histB_IsDownInt, histA_IsUpInt, hist, histA_IsDownInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( signal <= -2.17404 )
		if( hist <= 10.6881 )
			if( hist <= -1.7505 )
				if( hist <= -2.83901 )
					if( hist <= -6.61609 )
						if( signal <= -24.9563 )
							ret := -0.525641
						if( signal > -24.9563 )
							ret := -0.082386
					if( hist > -6.61609 )
						if( hist <= -5.5915 )
							ret := 0.427509
						if( hist > -5.5915 )
							ret := 0.028011
				if( hist > -2.83901 )
					if( macd <= -9.64179 )
						if( macd <= -20.5164 )
							ret := 0.013514
						if( macd > -20.5164 )
							ret := -0.706977 // sell
					if( macd > -9.64179 )
						if( macd <= -6.62916 )
							ret := 0.443396
						if( macd > -6.62916 )
							ret := 0.019608
			if( hist > -1.7505 )
				if( macd <= -21.6539 )
					if( signal <= -24.0303 )
						if( hist <= 0.099934 )
							ret := 0.705882 // buy
						if( hist > 0.099934 )
							ret := -0.089286
					if( signal > -24.0303 )
						if( hist <= -1.47326 )
							ret := -0.090909
						if( hist > -1.47326 )
							ret := -0.766234 // sell
				if( macd > -21.6539 )
					if( signal <= -22.8662 )
						if( histA_IsUpInt <= 0.5 )
							ret := 0.900000 // buy
						if( histA_IsUpInt > 0.5 )
							ret := 0.177778
					if( signal > -22.8662 )
						if( macd <= 0.322472 )
							ret := 0.117790
						if( macd > 0.322472 )
							ret := 0.393665
		if( hist > 10.6881 )
			if( signal <= -124.548 )
				if( signal <= -301.729 )
					if( macd <= -320.491 )
						ret := 1.000000 // buy
					if( macd > -320.491 )
						ret := 0.909091 // buy
				if( signal > -301.729 )
					ret := 0.454545
			if( signal > -124.548 )
				if( macd <= -3.51129 )
					if( hist <= 12.1459 )
						if( histA_IsUpInt <= 0.5 )
							ret := 0.615385
						if( histA_IsUpInt > 0.5 )
							ret := -0.058824
					if( hist > 12.1459 )
						if( macd <= -20.9656 )
							ret := -0.238095
						if( macd > -20.9656 )
							ret := -0.900000 // sell
				if( macd > -3.51129 )
					if( histA_IsUpInt <= 0.5 )
						if( histA_IsDownInt <= 0.5 )
							ret := -1.000000 // sell
						if( histA_IsDownInt > 0.5 )
							ret := -0.931034 // sell
					if( histA_IsUpInt > 0.5 )
						if( signal <= -12.8595 )
							ret := -1.000000 // sell
						if( signal > -12.8595 )
							ret := -0.490196
	if( signal > -2.17404 )
		if( macd <= -1.1419 )
			if( macd <= -1.52861 )
				if( hist <= -4.61671 )
					if( macd <= -2.89325 )
						if( signal <= 0.385393 )
							ret := -0.198630
						if( signal > 0.385393 )
							ret := -0.543269
					if( macd > -2.89325 )
						if( signal <= 3.41603 )
							ret := 0.578947
						if( signal > 3.41603 )
							ret := -0.250000
				if( hist > -4.61671 )
					if( hist <= -3.76338 )
						if( macd <= -4.14508 )
							ret := -0.160000
						if( macd > -4.14508 )
							ret := 0.698630
					if( hist > -3.76338 )
						if( histA_IsDownInt <= 0.5 )
							ret := -0.057471
						if( histA_IsDownInt > 0.5 )
							ret := 0.606061
			if( macd > -1.52861 )
				if( signal <= -1.3006 )
					if( hist <= 0.033933 )
						if( signal <= -1.39708 )
							ret := -0.796296 // sell
						if( signal > -1.39708 )
							ret := -0.970588 // sell
					if( hist > 0.033933 )
						if( hist <= 0.192006 )
							ret := 0.153846
						if( hist > 0.192006 )
							ret := -0.619355
				if( signal > -1.3006 )
					if( hist <= -0.139049 )
						if( signal <= 0.37164 )
							ret := -0.410569
						if( signal > 0.37164 )
							ret := 0.045977
					if( hist > -0.139049 )
						if( histA_IsUpInt <= 0.5 )
							ret := 0.448980
						if( histA_IsUpInt > 0.5 )
							ret := -0.785714 // sell
		if( macd > -1.1419 )
			if( macd <= -0.638631 )
				if( hist <= -0.081811 )
					if( signal <= 0.886904 )
						if( hist <= -0.616894 )
							ret := -0.371795
						if( hist > -0.616894 )
							ret := 0.036952
					if( signal > 0.886904 )
						if( signal <= 2.73272 )
							ret := 0.561644
						if( signal > 2.73272 )
							ret := -0.027778
				if( hist > -0.081811 )
					if( histB_IsUpInt <= 0.5 )
						if( signal <= -1.19257 )
							ret := 0.432836
						if( signal > -1.19257 )
							ret := 0.115903
					if( histB_IsUpInt > 0.5 )
						if( signal <= -0.730857 )
							ret := 0.711538 // buy
						if( signal > -0.730857 )
							ret := 0.324324
			if( macd > -0.638631 )
				if( macd <= 0.212651 )
					if( hist <= 0.115356 )
						if( signal <= -0.230561 )
							ret := 0.099775
						if( signal > -0.230561 )
							ret := -0.090645
					if( hist > 0.115356 )
						if( macd <= -0.396393 )
							ret := -0.400552
						if( macd > -0.396393 )
							ret := -0.087903
				if( macd > 0.212651 )
					if( signal <= 50.4815 )
						if( signal <= 15.6586 )
							ret := 0.012112
						if( signal > 15.6586 )
							ret := 0.151200
					if( signal > 50.4815 )
						if( hist <= -5.04304 )
							ret := -0.727273 // sell
						if( hist > -5.04304 )
							ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_GOOG_1Hour_3050d25f(macd, macd_IsBelowInt, signal, histB_IsUpInt, macd_IsAboveInt, histB_IsDownInt, histA_IsUpInt, hist, histA_IsDownInt)

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


