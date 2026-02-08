//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: ZI_30Min_1MAC_397c054b Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ZI_30Min_1MAC_397c054b", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ZI_30Min_397c054b(histB_IsUpInt, macd, histA_IsDownInt, hist, histB_IsDownInt, macd_IsAboveInt, signal, histA_IsUpInt, macd_IsBelowInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( macd_IsAboveInt <= 0.5 )
		if( signal <= 1.75346 )
			if( signal <= -1.09946 )
				if( histB_IsUpInt <= 0.5 )
					if( macd <= -1.47547 )
						ret := 0.909091 // buy
					if( macd > -1.47547 )
						ret := 1.000000 // buy
				if( histB_IsUpInt > 0.5 )
					if( macd <= -1.59876 )
						if( hist <= -0.068112 )
							ret := -0.204082
						if( hist > -0.068112 )
							ret := 0.750000 // buy
					if( macd > -1.59876 )
						if( macd <= -1.37813 )
							ret := 0.895833 // buy
						if( macd > -1.37813 )
							ret := 0.000000
			if( signal > -1.09946 )
				if( macd <= 0.268669 )
					if( hist <= -0.718166 )
						if( macd <= -1.3136 )
							ret := -0.238095
						if( macd > -1.3136 )
							ret := -0.714286 // sell
					if( hist > -0.718166 )
						if( macd <= 0.175983 )
							ret := 0.020148
						if( macd > 0.175983 )
							ret := 0.287151
				if( macd > 0.268669 )
					if( signal <= 0.366461 )
						if( macd <= 0.300787 )
							ret := -0.202703
						if( macd > 0.300787 )
							ret := -0.615385
					if( signal > 0.366461 )
						if( hist <= -0.041932 )
							ret := -0.115385
						if( hist > -0.041932 )
							ret := 0.174479
		if( signal > 1.75346 )
			if( histB_IsUpInt <= 0.5 )
				if( macd <= 2.1145 )
					if( signal <= 2.21227 )
						if( macd <= 1.53799 )
							ret := 0.647059
						if( macd > 1.53799 )
							ret := 0.942857 // buy
					if( signal > 2.21227 )
						ret := 0.555556
				if( macd > 2.1145 )
					ret := -1.000000 // sell
			if( histB_IsUpInt > 0.5 )
				ret := -0.500000
	if( macd_IsAboveInt > 0.5 )
		if( histA_IsUpInt <= 0.5 )
			if( macd <= -0.327137 )
				if( macd <= -0.633869 )
					if( macd <= -0.765422 )
						if( macd <= -1.09747 )
							ret := -0.523810
						if( macd > -1.09747 )
							ret := 0.210884
					if( macd > -0.765422 )
						if( signal <= -0.709427 )
							ret := -0.803922 // sell
						if( signal > -0.709427 )
							ret := 1.000000 // buy
				if( macd > -0.633869 )
					if( hist <= 0.227324 )
						if( macd <= -0.396258 )
							ret := 0.630522
						if( macd > -0.396258 )
							ret := 0.345324
					if( hist > 0.227324 )
						if( signal <= -0.730431 )
							ret := 0.000000
						if( signal > -0.730431 )
							ret := -0.700000 // sell
			if( macd > -0.327137 )
				if( macd <= -0.106885 )
					if( hist <= 0.129154 )
						if( signal <= -0.215819 )
							ret := 0.077982
						if( signal > -0.215819 )
							ret := -0.281250
					if( hist > 0.129154 )
						if( signal <= -0.618346 )
							ret := 0.812500 // buy
						if( signal > -0.618346 )
							ret := -0.587940
				if( macd > -0.106885 )
					if( signal <= -0.322884 )
						if( hist <= 0.450561 )
							ret := 0.333333
						if( hist > 0.450561 )
							ret := 0.891892 // buy
					if( signal > -0.322884 )
						if( hist <= 0.237074 )
							ret := 0.070857
						if( hist > 0.237074 )
							ret := -0.154143
		if( histA_IsUpInt > 0.5 )
			if( macd <= 0.334933 )
				if( signal <= -0.554184 )
					if( hist <= 0.158651 )
						if( signal <= -1.94514 )
							ret := 0.833333 // buy
						if( signal > -1.94514 )
							ret := -0.368175
					if( hist > 0.158651 )
						if( macd <= -1.68163 )
							ret := -0.791667 // sell
						if( macd > -1.68163 )
							ret := -0.022727
				if( signal > -0.554184 )
					if( signal <= -0.435749 )
						if( hist <= 0.084922 )
							ret := 0.544000
						if( hist > 0.084922 )
							ret := 0.172662
					if( signal > -0.435749 )
						if( signal <= -0.090677 )
							ret := -0.167598
						if( signal > -0.090677 )
							ret := -0.019950
			if( macd > 0.334933 )
				if( signal <= 0.353993 )
					if( hist <= 0.196841 )
						if( signal <= 0.221904 )
							ret := 0.454545
						if( signal > 0.221904 )
							ret := -0.282828
					if( hist > 0.196841 )
						if( signal <= 0.09673 )
							ret := -0.177419
						if( signal > 0.09673 )
							ret := -0.748603 // sell
				if( signal > 0.353993 )
					if( signal <= 0.551097 )
						if( signal <= 0.508947 )
							ret := -0.142292
						if( signal > 0.508947 )
							ret := 0.466667
					if( signal > 0.551097 )
						if( signal <= 0.679484 )
							ret := -0.666667
						if( signal > 0.679484 )
							ret := -0.157895
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_ZI_30Min_397c054b(histB_IsUpInt, macd, histA_IsDownInt, hist, histB_IsDownInt, macd_IsAboveInt, signal, histA_IsUpInt, macd_IsBelowInt)

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


