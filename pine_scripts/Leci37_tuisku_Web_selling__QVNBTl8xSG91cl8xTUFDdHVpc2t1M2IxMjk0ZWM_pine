//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: ASAN_1Hour_1MAC_3b1294ec Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ASAN_1Hour_1MAC_3b1294ec", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ASAN_1Hour_3b1294ec(macd_IsAboveInt, histB_IsDownInt, histA_IsDownInt, histB_IsUpInt, signal, histA_IsUpInt, hist, macd_IsBelowInt, macd)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( histA_IsDownInt <= 0.5 )
		if( hist <= 0.982312 )
			if( signal <= -1.48836 )
				if( hist <= -0.3413 )
					if( histB_IsDownInt <= 0.5 )
						if( macd <= -4.33991 )
							ret := -0.850000 // sell
						if( macd > -4.33991 )
							ret := 0.305556
					if( histB_IsDownInt > 0.5 )
						if( signal <= -2.14146 )
							ret := 0.000000
						if( signal > -2.14146 )
							ret := -0.915493 // sell
				if( hist > -0.3413 )
					if( hist <= 0.143452 )
						if( macd <= -1.45671 )
							ret := 0.450000
						if( macd > -1.45671 )
							ret := -0.833333 // sell
					if( hist > 0.143452 )
						if( signal <= -4.06442 )
							ret := 0.081081
						if( signal > -4.06442 )
							ret := -0.776978 // sell
			if( signal > -1.48836 )
				if( histB_IsUpInt <= 0.5 )
					if( signal <= 0.944776 )
						if( hist <= -0.082313 )
							ret := 0.128981
						if( hist > -0.082313 )
							ret := -0.021178
					if( signal > 0.944776 )
						if( hist <= -0.127236 )
							ret := -0.033149
						if( hist > -0.127236 )
							ret := -0.385542
				if( histB_IsUpInt > 0.5 )
					if( signal <= 0.315376 )
						if( macd <= 0.283417 )
							ret := -0.100313
						if( macd > 0.283417 )
							ret := 0.928571 // buy
					if( signal > 0.315376 )
						if( macd <= 0.000172 )
							ret := 0.636364
						if( macd > 0.000172 )
							ret := -0.324841
		if( hist > 0.982312 )
			if( macd <= -0.018458 )
				if( hist <= 1.7709 )
					if( macd <= -1.08667 )
						if( hist <= 0.994636 )
							ret := 0.750000 // buy
						if( hist > 0.994636 )
							ret := 1.000000 // buy
					if( macd > -1.08667 )
						ret := 0.714286 // buy
				if( hist > 1.7709 )
					ret := 0.285714
			if( macd > -0.018458 )
				if( hist <= 1.01968 )
					ret := 1.000000 // buy
				if( hist > 1.01968 )
					ret := -0.076923
	if( histA_IsDownInt > 0.5 )
		if( macd <= 0.150655 )
			if( hist <= 0.057493 )
				if( macd <= -0.413448 )
					if( signal <= -0.619082 )
						if( hist <= 0.006643 )
							ret := 1.000000 // buy
						if( hist > 0.006643 )
							ret := 0.434783
					if( signal > -0.619082 )
						if( macd <= -0.427971 )
							ret := -0.930233 // sell
						if( macd > -0.427971 )
							ret := -0.333333
				if( macd > -0.413448 )
					if( signal <= -0.336309 )
						if( hist <= 0.054317 )
							ret := 0.818182 // buy
						if( hist > 0.054317 )
							ret := 0.083333
					if( signal > -0.336309 )
						if( macd <= -0.239613 )
							ret := -0.571429
						if( macd > -0.239613 )
							ret := 0.092012
			if( hist > 0.057493 )
				if( hist <= 0.092732 )
					if( macd <= -0.02516 )
						if( signal <= -0.100671 )
							ret := 0.408935
						if( signal > -0.100671 )
							ret := -0.750000 // sell
					if( macd > -0.02516 )
						if( macd <= -0.0014 )
							ret := 0.959184 // buy
						if( macd > -0.0014 )
							ret := 0.521212
				if( hist > 0.092732 )
					if( hist <= 0.111135 )
						if( macd <= 0.012994 )
							ret := 0.071429
						if( macd > 0.012994 )
							ret := -0.323529
					if( hist > 0.111135 )
						if( signal <= -0.538652 )
							ret := 0.043478
						if( signal > -0.538652 )
							ret := 0.381657
		if( macd > 0.150655 )
			if( signal <= 0.655103 )
				if( hist <= 0.346009 )
					if( macd <= 0.18982 )
						if( signal <= 0.087359 )
							ret := 0.083333
						if( signal > 0.087359 )
							ret := -0.671233
					if( macd > 0.18982 )
						if( signal <= 0.622996 )
							ret := 0.015799
						if( signal > 0.622996 )
							ret := -0.511111
				if( hist > 0.346009 )
					if( hist <= 0.569102 )
						if( hist <= 0.421116 )
							ret := -0.333333
						if( hist > 0.421116 )
							ret := -0.900000 // sell
					if( hist > 0.569102 )
						if( macd <= 0.336495 )
							ret := 0.333333
						if( macd > 0.336495 )
							ret := 0.000000
			if( signal > 0.655103 )
				if( macd <= 1.12809 )
					if( signal <= 0.938857 )
						if( hist <= 0.049376 )
							ret := 0.800000 // buy
						if( hist > 0.049376 )
							ret := 0.459459
					if( signal > 0.938857 )
						if( signal <= 1.0411 )
							ret := 0.941176 // buy
						if( signal > 1.0411 )
							ret := 0.000000
				if( macd > 1.12809 )
					if( macd <= 1.41091 )
						if( signal <= 1.09641 )
							ret := 0.000000
						if( signal > 1.09641 )
							ret := -0.836735 // sell
					if( macd > 1.41091 )
						if( signal <= 1.16565 )
							ret := -0.150000
						if( signal > 1.16565 )
							ret := 0.233010
	
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
float op_operation = decision_tree_0_ASAN_1Hour_3b1294ec(macd_IsAboveInt, histB_IsDownInt, histA_IsDownInt, histB_IsUpInt, signal, histA_IsUpInt, hist, macd_IsBelowInt, macd)

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


