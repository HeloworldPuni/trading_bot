//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: TSLA_5Min_1MAC_a7a351c5 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TSLA_5Min_1MAC_a7a351c5", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TSLA_5Min_a7a351c5(histB_IsUpInt, macd_IsBelowInt, macd, histB_IsDownInt, macd_IsAboveInt, histA_IsDownInt, histA_IsUpInt, hist, signal)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.82,min_samples_leaf=7, min_samples_split=10,random_state=843828734)
	if( macd <= -0.565207 )
		if( hist <= -0.140648 )
			if( macd <= -0.892691 )
				if( signal <= -2.49185 )
					if( macd <= -4.3925 )
						ret := 0.900000 // buy
					if( macd > -4.3925 )
						if( signal <= -3.00608 )
							if( signal <= -3.0532 )
								ret := -0.714286 // sell
							if( signal > -3.0532 )
								ret := -1.000000 // sell
						if( signal > -3.00608 )
							if( signal <= -2.76331 )
								ret := -0.125000
							if( signal > -2.76331 )
								ret := -0.812500 // sell
				if( signal > -2.49185 )
					if( signal <= -1.33516 )
						if( signal <= -1.51739 )
							if( signal <= -1.95833 )
								ret := 0.477273
							if( signal > -1.95833 )
								ret := 0.020000
						if( signal > -1.51739 )
							if( macd <= -2.14943 )
								ret := -0.250000
							if( macd > -2.14943 )
								ret := 0.617143
					if( signal > -1.33516 )
						if( macd <= -2.28197 )
							if( signal <= -0.910058 )
								ret := -0.906250 // sell
							if( signal > -0.910058 )
								ret := 0.900000 // buy
						if( macd > -2.28197 )
							if( hist <= -0.184814 )
								ret := 0.143449
							if( hist > -0.184814 )
								ret := -0.133333
			if( macd > -0.892691 )
				if( macd <= -0.864414 )
					if( hist <= -0.191097 )
						if( macd <= -0.881688 )
							if( macd <= -0.890648 )
								ret := -0.222222
							if( macd > -0.890648 )
								ret := 0.588235
						if( macd > -0.881688 )
							if( signal <= -0.393039 )
								ret := -0.653846
							if( signal > -0.393039 )
								ret := -0.277778
					if( hist > -0.191097 )
						if( histB_IsUpInt <= 0.5 )
							ret := -1.000000 // sell
						if( histB_IsUpInt > 0.5 )
							if( hist <= -0.162436 )
								ret := -0.714286 // sell
							if( hist > -0.162436 )
								ret := -0.714286 // sell
				if( macd > -0.864414 )
					if( signal <= -0.093877 )
						if( macd <= -0.858124 )
							if( signal <= -0.551122 )
								ret := 0.793103 // buy
							if( signal > -0.551122 )
								ret := -0.142857
						if( macd > -0.858124 )
							if( macd <= -0.780481 )
								ret := 0.029358
							if( macd > -0.780481 )
								ret := -0.112056
					if( signal > -0.093877 )
						if( signal <= 0.038738 )
							if( hist <= -0.72874 )
								ret := 0.894737 // buy
							if( hist > -0.72874 )
								ret := 0.615385
						if( signal > 0.038738 )
							if( hist <= -0.747009 )
								ret := -0.583333
							if( hist > -0.747009 )
								ret := 0.300000
		if( hist > -0.140648 )
			if( signal <= -0.991617 )
				if( macd <= -2.78222 )
					if( hist <= 0.560606 )
						if( macd <= -3.04619 )
							if( signal <= -3.45385 )
								ret := 0.708333 // buy
							if( signal > -3.45385 )
								ret := 0.935484 // buy
						if( macd > -3.04619 )
							if( histA_IsUpInt <= 0.5 )
								ret := 0.153846
							if( histA_IsUpInt > 0.5 )
								ret := 0.909091 // buy
					if( hist > 0.560606 )
						ret := -0.875000 // sell
				if( macd > -2.78222 )
					if( hist <= -0.065685 )
						if( signal <= -1.35093 )
							if( signal <= -1.78535 )
								ret := 0.066667
							if( signal > -1.78535 )
								ret := 0.686747
						if( signal > -1.35093 )
							if( macd <= -1.36719 )
								ret := -0.315789
							if( macd > -1.36719 )
								ret := 0.240876
					if( hist > -0.065685 )
						if( signal <= -2.76845 )
							if( signal <= -2.80348 )
								ret := -0.857143 // sell
							if( signal > -2.80348 )
								ret := -0.437500
						if( signal > -2.76845 )
							if( hist <= 0.513078 )
								ret := -0.039851
							if( hist > 0.513078 )
								ret := 0.472826
			if( signal > -0.991617 )
				if( histB_IsUpInt <= 0.5 )
					if( macd <= -0.83614 )
						if( signal <= -0.926952 )
							if( macd <= -0.946003 )
								ret := 0.076923
							if( macd > -0.946003 )
								ret := 0.609272
						if( signal > -0.926952 )
							if( macd <= -0.909629 )
								ret := 0.527778
							if( macd > -0.909629 )
								ret := 0.010101
					if( macd > -0.83614 )
						if( macd <= -0.569167 )
							if( signal <= -0.672209 )
								ret := 0.074482
							if( signal > -0.672209 )
								ret := 0.241814
						if( macd > -0.569167 )
							if( macd <= -0.568043 )
								ret := 1.000000 // buy
							if( macd > -0.568043 )
								ret := 0.431818
				if( histB_IsUpInt > 0.5 )
					if( signal <= -0.936521 )
						if( macd <= -1.10136 )
							ret := 0.142857
						if( macd > -1.10136 )
							if( signal <= -0.952364 )
								ret := 0.666667
							if( signal > -0.952364 )
								ret := 0.961538 // buy
					if( signal > -0.936521 )
						if( macd <= -0.799084 )
							if( hist <= -0.064959 )
								ret := -0.023041
							if( hist > -0.064959 )
								ret := 0.398693
						if( macd > -0.799084 )
							if( macd <= -0.747487 )
								ret := 0.780952 // buy
							if( macd > -0.747487 )
								ret := 0.305118
	if( macd > -0.565207 )
		if( hist <= -0.044809 )
			if( macd <= 1.33089 )
				if( hist <= -0.222119 )
					if( macd <= -0.556897 )
						if( signal <= -0.237212 )
							if( signal <= -0.281595 )
								ret := -0.555556
							if( signal > -0.281595 )
								ret := 0.625000
						if( signal > -0.237212 )
							if( signal <= -0.213335 )
								ret := -1.000000 // sell
							if( signal > -0.213335 )
								ret := -0.628571
					if( macd > -0.556897 )
						if( signal <= -0.291138 )
							if( macd <= -0.547086 )
								ret := -1.000000 // sell
							if( macd > -0.547086 )
								ret := -0.500000
						if( signal > -0.291138 )
							if( signal <= -0.252433 )
								ret := 0.590164
							if( signal > -0.252433 )
								ret := 0.056330
				if( hist > -0.222119 )
					if( macd <= 0.712719 )
						if( macd <= 0.12472 )
							if( macd <= -0.163173 )
								ret := 0.028476
							if( macd > -0.163173 )
								ret := -0.064516
						if( macd > 0.12472 )
							if( signal <= 0.202331 )
								ret := 0.369863
							if( signal > 0.202331 )
								ret := 0.026662
					if( macd > 0.712719 )
						if( macd <= 0.781598 )
							if( signal <= 0.877525 )
								ret := -0.207407
							if( signal > 0.877525 )
								ret := -0.500000
						if( macd > 0.781598 )
							if( macd <= 0.821001 )
								ret := 0.183333
							if( macd > 0.821001 )
								ret := -0.108382
			if( macd > 1.33089 )
				if( signal <= 1.53425 )
					if( macd <= 1.36502 )
						if( hist <= -0.146509 )
							ret := 0.714286 // buy
						if( hist > -0.146509 )
							if( macd <= 1.34789 )
								ret := 1.000000 // buy
							if( macd > 1.34789 )
								ret := 0.909091 // buy
					if( macd > 1.36502 )
						if( signal <= 1.5159 )
							ret := 0.300000
						if( signal > 1.5159 )
							ret := 0.888889 // buy
				if( signal > 1.53425 )
					if( signal <= 1.56543 )
						if( hist <= -0.149632 )
							ret := -1.000000 // sell
						if( hist > -0.149632 )
							ret := -0.444444
					if( signal > 1.56543 )
						if( hist <= -0.691401 )
							if( macd <= 3.25723 )
								ret := 0.666667
							if( macd > 3.25723 )
								ret := 1.000000 // buy
						if( hist > -0.691401 )
							if( signal <= 1.74863 )
								ret := 0.337143
							if( signal > 1.74863 )
								ret := 0.088235
		if( hist > -0.044809 )
			if( signal <= 0.711774 )
				if( macd <= -0.00279 )
					if( macd <= -0.048793 )
						if( signal <= -0.217751 )
							if( macd <= -0.07501 )
								ret := 0.016663
							if( macd > -0.07501 )
								ret := 0.300546
						if( signal > -0.217751 )
							if( signal <= -0.178903 )
								ret := 0.174704
							if( signal > -0.178903 )
								ret := 0.049980
					if( macd > -0.048793 )
						if( signal <= -0.207623 )
							if( histA_IsUpInt <= 0.5 )
								ret := -0.011111
							if( histA_IsUpInt > 0.5 )
								ret := -0.433155
						if( signal > -0.207623 )
							if( signal <= 0.004454 )
								ret := -0.012238
							if( signal > 0.004454 )
								ret := 0.183007
				if( macd > -0.00279 )
					if( hist <= 0.070736 )
						if( signal <= 0.669262 )
							if( macd <= 0.355144 )
								ret := 0.115869
							if( macd > 0.355144 )
								ret := 0.038914
						if( signal > 0.669262 )
							if( macd <= 0.724811 )
								ret := 0.641304
							if( macd > 0.724811 )
								ret := 0.117647
					if( hist > 0.070736 )
						if( hist <= 0.412663 )
							if( macd <= 0.929341 )
								ret := 0.056418
							if( macd > 0.929341 )
								ret := 0.360294
						if( hist > 0.412663 )
							if( signal <= 0.672562 )
								ret := 0.154793
							if( signal > 0.672562 )
								ret := -0.306122
			if( signal > 0.711774 )
				if( hist <= 1.11476 )
					if( signal <= 1.86911 )
						if( macd <= 1.87506 )
							if( hist <= 0.812469 )
								ret := -0.045337
							if( hist > 0.812469 )
								ret := -0.800000 // sell
						if( macd > 1.87506 )
							if( signal <= 1.05709 )
								ret := -0.866667 // sell
							if( signal > 1.05709 )
								ret := -0.278539
					if( signal > 1.86911 )
						if( macd <= 2.81249 )
							if( hist <= 0.144047 )
								ret := 0.600000
							if( hist > 0.144047 )
								ret := 0.144578
						if( macd > 2.81249 )
							if( hist <= 0.512385 )
								ret := -0.700000 // sell
							if( hist > 0.512385 )
								ret := 0.454545
				if( hist > 1.11476 )
					if( hist <= 1.86696 )
						if( macd <= 3.02564 )
							ret := 0.583333
						if( macd > 3.02564 )
							if( macd <= 3.63153 )
								ret := 1.000000 // buy
							if( macd > 3.63153 )
								ret := 0.857143 // buy
					if( hist > 1.86696 )
						ret := -0.111111
	
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
float op_operation = decision_tree_0_TSLA_5Min_a7a351c5(histB_IsUpInt, macd_IsBelowInt, macd, histB_IsDownInt, macd_IsAboveInt, histA_IsDownInt, histA_IsUpInt, hist, signal)

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


