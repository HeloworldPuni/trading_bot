//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: XRPUSDT_30Min_1MAC_9cb82bb7 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_XRPUSDT_30Min_1MAC_9cb82bb7", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_XRPUSDT_30Min_9cb82bb7(histB_IsUpInt, macd, histA_IsDownInt, hist, histB_IsDownInt, macd_IsAboveInt, signal, histA_IsUpInt, macd_IsBelowInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7,max_features=sqrt, min_samples_leaf=4,random_state=843828734)
	if( signal <= -0.00083 )
		if( histB_IsDownInt <= 0.5 )
			if( macd <= -0.002133 )
				if( hist <= 0.021186 )
					if( signal <= -0.03726 )
						if( macd <= -0.05915 )
							if( histA_IsDownInt <= 0.5 )
								ret := 0.084507
							if( histA_IsDownInt > 0.5 )
								ret := -0.866667 // sell
						if( macd > -0.05915 )
							if( macd <= -0.031835 )
								ret := 0.602459
							if( macd > -0.031835 )
								ret := 0.000000
					if( signal > -0.03726 )
						if( macd <= -0.007177 )
							if( signal <= -0.004959 )
								ret := -0.032562
							if( signal > -0.004959 )
								ret := -0.422053
						if( macd > -0.007177 )
							if( histA_IsUpInt <= 0.5 )
								ret := 0.113525
							if( histA_IsUpInt > 0.5 )
								ret := 0.002033
				if( hist > 0.021186 )
					if( hist <= 0.024076 )
						ret := -0.897436 // sell
					if( hist > 0.024076 )
						ret := -0.500000
			if( macd > -0.002133 )
				if( signal <= -0.0031 )
					if( signal <= -0.005609 )
						if( signal <= -0.009043 )
							if( signal <= -0.010433 )
								ret := -0.176471
							if( signal > -0.010433 )
								ret := -0.933333 // sell
						if( signal > -0.009043 )
							if( histA_IsUpInt <= 0.5 )
								ret := 0.559140
							if( histA_IsUpInt > 0.5 )
								ret := 0.165217
					if( signal > -0.005609 )
						if( signal <= -0.003863 )
							if( histA_IsDownInt <= 0.5 )
								ret := -0.350000
							if( histA_IsDownInt > 0.5 )
								ret := -0.321739
						if( signal > -0.003863 )
							if( hist <= 0.001341 )
								ret := -0.662338
							if( hist > 0.001341 )
								ret := -0.087413
				if( signal > -0.0031 )
					if( macd_IsAboveInt <= 0.5 )
						if( macd <= -0.001273 )
							if( hist <= -0.000903 )
								ret := -0.446602
							if( hist > -0.000903 )
								ret := -0.011152
						if( macd > -0.001273 )
							if( signal <= -0.001062 )
								ret := -0.616667
							if( signal > -0.001062 )
								ret := -0.145228
					if( macd_IsAboveInt > 0.5 )
						if( macd <= 0.000341 )
							if( hist <= 0.002647 )
								ret := -0.003717
							if( hist > 0.002647 )
								ret := 0.442857
						if( macd > 0.000341 )
							if( macd <= 0.002345 )
								ret := 0.166667
							if( macd > 0.002345 )
								ret := -0.117391
		if( histB_IsDownInt > 0.5 )
			if( signal <= -0.014631 )
				if( macd <= -0.0408 )
					if( hist <= -0.012078 )
						if( macd <= -0.050498 )
							if( signal <= -0.038063 )
								ret := 0.000000
							if( signal > -0.038063 )
								ret := -0.916667 // sell
						if( macd > -0.050498 )
							if( macd <= -0.044775 )
								ret := 0.411765
							if( macd > -0.044775 )
								ret := -0.900000 // sell
					if( hist > -0.012078 )
						if( signal <= -0.062781 )
							ret := -0.333333
						if( signal > -0.062781 )
							if( macd <= -0.044431 )
								ret := 0.945946 // buy
							if( macd > -0.044431 )
								ret := -0.333333
				if( macd > -0.0408 )
					if( hist <= -0.001697 )
						if( signal <= -0.023892 )
							if( macd <= -0.029645 )
								ret := 0.596154
							if( macd > -0.029645 )
								ret := -0.666667
						if( signal > -0.023892 )
							if( macd <= -0.028394 )
								ret := 1.000000 // buy
							if( macd > -0.028394 )
								ret := 0.767123 // buy
					if( hist > -0.001697 )
						if( hist <= -0.000374 )
							if( macd <= -0.021287 )
								ret := 0.526316
							if( macd > -0.021287 )
								ret := -0.346154
						if( hist > -0.000374 )
							ret := 1.000000 // buy
			if( signal > -0.014631 )
				if( signal <= -0.011083 )
					if( hist <= -0.011458 )
						if( macd <= -0.029625 )
							if( signal <= -0.01246 )
								ret := 0.333333
							if( signal > -0.01246 )
								ret := 0.000000
						if( macd > -0.029625 )
							ret := 1.000000 // buy
					if( hist > -0.011458 )
						if( macd <= -0.016822 )
							if( macd <= -0.018757 )
								ret := -0.425532
							if( macd > -0.018757 )
								ret := -0.972973 // sell
						if( macd > -0.016822 )
							if( signal <= -0.012044 )
								ret := 0.103448
							if( signal > -0.012044 )
								ret := -0.714286 // sell
				if( signal > -0.011083 )
					if( macd <= -0.007287 )
						if( signal <= -0.008625 )
							if( macd <= -0.010815 )
								ret := 0.303887
							if( macd > -0.010815 )
								ret := -0.607843
						if( signal > -0.008625 )
							if( macd <= -0.012112 )
								ret := 0.828358 // buy
							if( macd > -0.012112 )
								ret := 0.337838
					if( macd > -0.007287 )
						if( signal <= -0.005483 )
							if( macd <= -0.006934 )
								ret := -0.619048
							if( macd > -0.006934 )
								ret := 0.109890
						if( signal > -0.005483 )
							if( signal <= -0.00474 )
								ret := 0.623077
							if( signal > -0.00474 )
								ret := 0.104146
	if( signal > -0.00083 )
		if( macd_IsAboveInt <= 0.5 )
			if( hist <= -0.002066 )
				if( signal <= 0.001458 )
					if( histB_IsUpInt <= 0.5 )
						if( hist <= -0.002348 )
							if( signal <= 7e-06 )
								ret := 0.351852
							if( signal > 7e-06 )
								ret := 0.616751
						if( hist > -0.002348 )
							if( hist <= -0.002105 )
								ret := 0.182482
							if( hist > -0.002105 )
								ret := -0.500000
					if( histB_IsUpInt > 0.5 )
						if( hist <= -0.00274 )
							if( hist <= -0.006444 )
								ret := -0.666667
							if( hist > -0.006444 )
								ret := -0.049505
						if( hist > -0.00274 )
							if( macd <= -0.002383 )
								ret := 0.506024
							if( macd > -0.002383 )
								ret := 0.248175
				if( signal > 0.001458 )
					if( macd <= -0.000786 )
						if( histB_IsUpInt <= 0.5 )
							if( signal <= 0.009513 )
								ret := -0.055710
							if( signal > 0.009513 )
								ret := 0.600000
						if( histB_IsUpInt > 0.5 )
							if( hist <= -0.00375 )
								ret := -0.429245
							if( hist > -0.00375 )
								ret := -0.768116 // sell
					if( macd > -0.000786 )
						if( histB_IsDownInt <= 0.5 )
							if( signal <= 0.002727 )
								ret := 0.323077
							if( signal > 0.002727 )
								ret := -0.077352
						if( histB_IsDownInt > 0.5 )
							if( hist <= -0.002089 )
								ret := 0.112817
							if( hist > -0.002089 )
								ret := 0.736842 // buy
			if( hist > -0.002066 )
				if( histB_IsDownInt <= 0.5 )
					if( macd <= -0.002202 )
						if( macd <= -0.002329 )
							if( hist <= -0.00179 )
								ret := -0.545455
							if( hist > -0.00179 )
								ret := 0.000000
						if( macd > -0.002329 )
							if( hist <= -0.001795 )
								ret := -0.800000 // sell
							if( hist > -0.001795 )
								ret := -1.000000 // sell
					if( macd > -0.002202 )
						if( macd <= -0.001873 )
							if( hist <= -0.001758 )
								ret := 0.340426
							if( hist > -0.001758 )
								ret := 0.762500 // buy
						if( macd > -0.001873 )
							if( hist <= -0.001913 )
								ret := -0.414815
							if( hist > -0.001913 )
								ret := -0.007331
				if( histB_IsDownInt > 0.5 )
					if( hist <= -0.000172 )
						if( hist <= -0.001932 )
							if( signal <= 0.002509 )
								ret := -0.400000
							if( signal > 0.002509 )
								ret := 0.015228
						if( hist > -0.001932 )
							if( macd <= 0.000481 )
								ret := -0.089630
							if( macd > 0.000481 )
								ret := 0.009514
					if( hist > -0.000172 )
						if( signal <= -0.000371 )
							if( macd <= -0.000733 )
								ret := 0.088608
							if( macd > -0.000733 )
								ret := -0.333333
						if( signal > -0.000371 )
							if( macd <= 0.001847 )
								ret := 0.016799
							if( macd > 0.001847 )
								ret := 0.184543
		if( macd_IsAboveInt > 0.5 )
			if( macd <= 0.002983 )
				if( macd <= 0.002923 )
					if( signal <= 0.002572 )
						if( histA_IsDownInt <= 0.5 )
							if( signal <= -0.000612 )
								ret := -0.149062
							if( signal > -0.000612 )
								ret := 0.030549
						if( histA_IsDownInt > 0.5 )
							if( signal <= 0.002322 )
								ret := -0.023810
							if( signal > 0.002322 )
								ret := 0.284722
					if( signal > 0.002572 )
						if( hist <= 0.000116 )
							if( hist <= 0.000107 )
								ret := -0.369231
							if( hist > 0.000107 )
								ret := 0.750000 // buy
						if( hist > 0.000116 )
							if( histA_IsDownInt <= 0.5 )
								ret := -0.857143 // sell
							if( histA_IsDownInt > 0.5 )
								ret := -0.705882 // sell
				if( macd > 0.002923 )
					if( signal <= -0.000136 )
						ret := 1.000000 // buy
					if( signal > -0.000136 )
						if( signal <= 0.000675 )
							ret := -0.642857
						if( signal > 0.000675 )
							if( histA_IsDownInt <= 0.5 )
								ret := 0.465753
							if( histA_IsDownInt > 0.5 )
								ret := 0.406250
			if( macd > 0.002983 )
				if( signal <= 0.007671 )
					if( histA_IsDownInt <= 0.5 )
						if( macd <= 0.006151 )
							if( hist <= 0.002591 )
								ret := -0.171429
							if( hist > 0.002591 )
								ret := -0.003752
						if( macd > 0.006151 )
							if( macd <= 0.007684 )
								ret := -0.403780
							if( macd > 0.007684 )
								ret := -0.149020
					if( histA_IsDownInt > 0.5 )
						if( hist <= 0.002553 )
							if( macd <= 0.00561 )
								ret := -0.053535
							if( macd > 0.00561 )
								ret := -0.264818
						if( hist > 0.002553 )
							if( macd <= 0.017682 )
								ret := -0.279070
							if( macd > 0.017682 )
								ret := 0.916667 // buy
				if( signal > 0.007671 )
					if( macd <= 0.009056 )
						if( signal <= 0.008678 )
							if( signal <= 0.007799 )
								ret := 0.050000
							if( signal > 0.007799 )
								ret := -0.610526
						if( signal > 0.008678 )
							ret := 0.500000
					if( macd > 0.009056 )
						if( histA_IsDownInt <= 0.5 )
							if( hist <= 0.006823 )
								ret := 0.106632
							if( hist > 0.006823 )
								ret := -0.352542
						if( histA_IsDownInt > 0.5 )
							if( hist <= 0.000123 )
								ret := 0.857143 // buy
							if( hist > 0.000123 )
								ret := -0.016402
	
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
float op_operation = decision_tree_0_XRPUSDT_30Min_9cb82bb7(histB_IsUpInt, macd, histA_IsDownInt, hist, histB_IsDownInt, macd_IsAboveInt, signal, histA_IsUpInt, macd_IsBelowInt)

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


