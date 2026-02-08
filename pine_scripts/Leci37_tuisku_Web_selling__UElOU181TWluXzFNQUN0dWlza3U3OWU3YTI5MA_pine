//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: PINS_5Min_1MAC_79e7a290 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PINS_5Min_1MAC_79e7a290", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PINS_5Min_79e7a290(macd, macd_IsBelowInt, signal, histB_IsUpInt, macd_IsAboveInt, histB_IsDownInt, histA_IsUpInt, hist, histA_IsDownInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( histA_IsUpInt <= 0.5 )
		if( signal <= 0.028632 )
			if( histB_IsDownInt <= 0.5 )
				if( hist <= -0.299081 )
					if( macd <= -1.36131 )
						ret := 1.000000 // buy
					if( macd > -1.36131 )
						ret := 0.200000
				if( hist > -0.299081 )
					if( signal <= -0.170136 )
						if( hist <= -0.061729 )
							ret := -0.242188
						if( hist > -0.061729 )
							ret := 0.299689
					if( signal > -0.170136 )
						if( signal <= -0.066392 )
							ret := -0.058856
						if( signal > -0.066392 )
							ret := 0.041928
			if( histB_IsDownInt > 0.5 )
				if( hist <= -0.00667 )
					if( macd <= 0.006072 )
						if( hist <= -0.221918 )
							ret := -0.574074
						if( hist > -0.221918 )
							ret := 0.144380
					if( macd > 0.006072 )
						if( hist <= -0.017275 )
							ret := 0.893617 // buy
						if( hist > -0.017275 )
							ret := 0.345882
				if( hist > -0.00667 )
					if( signal <= -0.112931 )
						if( macd <= -0.188274 )
							ret := 0.583333
						if( macd > -0.188274 )
							ret := 0.860000 // buy
					if( signal > -0.112931 )
						if( signal <= -0.058038 )
							ret := -0.443089
						if( signal > -0.058038 )
							ret := 0.043253
		if( signal > 0.028632 )
			if( signal <= 0.137554 )
				if( macd <= -0.026861 )
					if( hist <= -0.163542 )
						ret := -0.500000
					if( hist > -0.163542 )
						if( signal <= 0.114486 )
							ret := 0.742574 // buy
						if( signal > 0.114486 )
							ret := -1.000000 // sell
				if( macd > -0.026861 )
					if( hist <= 0.053214 )
						if( macd <= 0.023467 )
							ret := -0.142340
						if( macd > 0.023467 )
							ret := 0.014152
					if( hist > 0.053214 )
						if( macd <= 0.21205 )
							ret := 0.447293
						if( macd > 0.21205 )
							ret := -0.254545
			if( signal > 0.137554 )
				if( signal <= 0.206381 )
					if( hist <= -0.100101 )
						if( signal <= 0.168207 )
							ret := -0.700000 // sell
						if( signal > 0.168207 )
							ret := -1.000000 // sell
					if( hist > -0.100101 )
						if( hist <= -0.051893 )
							ret := 0.358491
						if( hist > -0.051893 )
							ret := -0.171233
				if( signal > 0.206381 )
					if( macd <= 0.191242 )
						if( macd <= 0.093066 )
							ret := -1.000000 // sell
						if( macd > 0.093066 )
							ret := 0.472050
					if( macd > 0.191242 )
						if( hist <= -0.041913 )
							ret := -0.291080
						if( hist > -0.041913 )
							ret := 0.038591
	if( histA_IsUpInt > 0.5 )
		if( signal <= -0.085378 )
			if( hist <= 0.066928 )
				if( macd <= -0.158079 )
					if( macd <= -0.378482 )
						if( hist <= 0.030791 )
							ret := 0.250000
						if( hist > 0.030791 )
							ret := -0.700000 // sell
					if( macd > -0.378482 )
						if( signal <= -0.208375 )
							ret := 0.704846 // buy
						if( signal > -0.208375 )
							ret := 0.266667
				if( macd > -0.158079 )
					if( hist <= 0.015369 )
						if( macd <= -0.083714 )
							ret := 0.121597
						if( macd > -0.083714 )
							ret := 0.394958
					if( hist > 0.015369 )
						if( signal <= -0.092031 )
							ret := -0.069317
						if( signal > -0.092031 )
							ret := 0.236111
			if( hist > 0.066928 )
				if( macd <= -0.031775 )
					if( signal <= -0.353633 )
						if( hist <= 0.124957 )
							ret := 0.232558
						if( hist > 0.124957 )
							ret := -0.840000 // sell
					if( signal > -0.353633 )
						if( signal <= -0.109104 )
							ret := -0.747059 // sell
						if( signal > -0.109104 )
							ret := 1.000000 // buy
				if( macd > -0.031775 )
					if( signal <= -0.094592 )
						if( signal <= -0.101778 )
							ret := 1.000000 // buy
						if( signal > -0.101778 )
							ret := 0.666667
					if( signal > -0.094592 )
						ret := -0.400000
		if( signal > -0.085378 )
			if( signal <= 0.277695 )
				if( macd <= 0.287246 )
					if( signal <= 0.03888 )
						if( signal <= -0.006264 )
							ret := -0.147262
						if( signal > -0.006264 )
							ret := -0.057011
					if( signal > 0.03888 )
						if( hist <= 0.081819 )
							ret := -0.169145
						if( hist > 0.081819 )
							ret := -0.554286
				if( macd > 0.287246 )
					if( macd <= 0.638539 )
						if( signal <= 0.271696 )
							ret := -1.000000 // sell
						if( signal > 0.271696 )
							ret := -0.500000
					if( macd > 0.638539 )
						ret := 1.000000 // buy
			if( signal > 0.277695 )
				ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_PINS_5Min_79e7a290(macd, macd_IsBelowInt, signal, histB_IsUpInt, macd_IsAboveInt, histB_IsDownInt, histA_IsUpInt, hist, histA_IsDownInt)

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


