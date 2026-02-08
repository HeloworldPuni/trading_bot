//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Vortex_Indicator
// ID_model: PINS_30Min_2BV0_ae339606 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PINS_30Min_2BV0_ae339606", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PINS_30Min_ae339606(bearPower, bbm, bbp, bullPower, BBPower_Color, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( bullPower <= -0.221389 )
		if( bearPower <= -0.422156 )
			if( bbp <= -0.873155 )
				if( bearPower <= -1.42091 )
					if( bearPower <= -1.89001 )
						if( bullPower <= -1.67416 )
							ret := -0.222222
						if( bullPower > -1.67416 )
							ret := 0.374532
					if( bearPower > -1.89001 )
						if( VIP <= 1.032 )
							ret := -0.334076
						if( VIP > 1.032 )
							ret := 0.551724
				if( bearPower > -1.42091 )
					if( VIP_VIM <= -0.946018 )
						if( bbm <= 0.160086 )
							ret := -0.222222
						if( bbm > 0.160086 )
							ret := 0.819277 // buy
					if( VIP_VIM > -0.946018 )
						if( bbp <= -2.27374 )
							ret := 0.651515
						if( bbp > -2.27374 )
							ret := 0.180956
			if( bbp > -0.873155 )
				if( VIM <= 1.63384 )
					if( VIM <= 1.25831 )
						if( VIM <= 1.17694 )
							ret := -0.380597
						if( VIM > 1.17694 )
							ret := 0.148148
					if( VIM > 1.25831 )
						if( VIP_VIM <= -0.73121 )
							ret := 0.181818
						if( VIP_VIM > -0.73121 )
							ret := -0.433908
				if( VIM > 1.63384 )
					if( bearPower <= -0.503348 )
						ret := 0.000000
					if( bearPower > -0.503348 )
						if( bullPower <= -0.287879 )
							ret := 0.785714 // buy
						if( bullPower > -0.287879 )
							ret := 1.000000 // buy
		if( bearPower > -0.422156 )
			if( VIP <= 0.75131 )
				if( VIP_VIM <= -0.635849 )
					if( bearPower <= -0.414998 )
						ret := -0.777778 // sell
					if( bearPower > -0.414998 )
						if( bearPower <= -0.389378 )
							ret := 0.045455
						if( bearPower > -0.389378 )
							ret := -0.463415
				if( VIP_VIM > -0.635849 )
					if( VIM <= 1.31413 )
						if( VIP_VIM <= -0.60286 )
							ret := -1.000000 // sell
						if( VIP_VIM > -0.60286 )
							ret := 0.000000
					if( VIM > 1.31413 )
						ret := 0.545455
			if( VIP > 0.75131 )
				if( VIP <= 1.05231 )
					if( bbm <= 0.051375 )
						if( bullPower <= -0.403408 )
							ret := 0.923077 // buy
						if( bullPower > -0.403408 )
							ret := 0.125954
					if( bbm > 0.051375 )
						if( bbp <= -0.623664 )
							ret := 0.279330
						if( bbp > -0.623664 )
							ret := 0.685714
				if( VIP > 1.05231 )
					if( bearPower <= -0.243188 )
						if( VIP <= 1.48416 )
							ret := 0.523810
						if( VIP > 1.48416 )
							ret := 0.880000 // buy
					if( bearPower > -0.243188 )
						if( VIP <= 1.50887 )
							ret := 0.500000
						if( VIP > 1.50887 )
							ret := -0.857143 // sell
	if( bullPower > -0.221389 )
		if( bearPower <= 0.083929 )
			if( VIP <= 0.899576 )
				if( bearPower <= -0.84247 )
					if( VIP_VIM <= -0.625409 )
						if( bullPower <= -0.216324 )
							ret := -1.000000 // sell
						if( bullPower > -0.216324 )
							ret := 0.536585
					if( VIP_VIM > -0.625409 )
						if( bullPower <= -0.132506 )
							ret := -0.658537
						if( bullPower > -0.132506 )
							ret := -0.215726
				if( bearPower > -0.84247 )
					if( VIP_VIM <= -0.278363 )
						if( VIM <= 1.09031 )
							ret := -0.846154 // sell
						if( VIM > 1.09031 )
							ret := -0.022935
					if( VIP_VIM > -0.278363 )
						if( bbp <= -0.132248 )
							ret := -0.203582
						if( bbp > -0.132248 )
							ret := -0.012526
			if( VIP > 0.899576 )
				if( VIM <= 1.91768 )
					if( bbp <= -0.354099 )
						if( VIP <= 0.932771 )
							ret := -0.014368
						if( VIP > 0.932771 )
							ret := 0.157789
					if( bbp > -0.354099 )
						if( bearPower <= -0.207506 )
							ret := -0.064581
						if( bearPower > -0.207506 )
							ret := 0.030424
				if( VIM > 1.91768 )
					if( bearPower <= -0.07457 )
						if( bbm <= 0.20833 )
							ret := 0.670455
						if( bbm > 0.20833 )
							ret := 0.176471
					if( bearPower > -0.07457 )
						if( bbp <= -0.047439 )
							ret := -0.781250 // sell
						if( bbp > -0.047439 )
							ret := 0.135714
		if( bearPower > 0.083929 )
			if( VIP_VIM <= 0.320334 )
				if( VIP <= 1.29632 )
					if( VIM <= 1.60203 )
						if( VIM <= 0.850987 )
							ret := -0.437158
						if( VIM > 0.850987 )
							ret := -0.077222
					if( VIM > 1.60203 )
						if( VIM <= 1.74895 )
							ret := -0.886076 // sell
						if( VIM > 1.74895 )
							ret := -0.045455
				if( VIP > 1.29632 )
					if( VIP <= 1.74313 )
						if( VIM <= 1.43584 )
							ret := -0.412946
						if( VIM > 1.43584 )
							ret := -0.715719 // sell
					if( VIP > 1.74313 )
						if( VIP_VIM <= -0.210432 )
							ret := -0.800000 // sell
						if( VIP_VIM > -0.210432 )
							ret := 0.446602
			if( VIP_VIM > 0.320334 )
				if( VIM <= 0.937931 )
					if( bearPower <= 2.19126 )
						if( bearPower <= 1.11953 )
							ret := 0.047848
						if( bearPower > 1.11953 )
							ret := -0.433962
					if( bearPower > 2.19126 )
						if( bbm <= 1.36447 )
							ret := 0.803030 // buy
						if( bbm > 1.36447 )
							ret := -0.071429
				if( VIM > 0.937931 )
					if( bearPower <= 0.436032 )
						if( VIM <= 1.29654 )
							ret := -0.112903
						if( VIM > 1.29654 )
							ret := -0.558824
					if( bearPower > 0.436032 )
						if( bearPower <= 0.645808 )
							ret := -0.883721 // sell
						if( bearPower > 0.645808 )
							ret := -0.096774
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_PINS_30Min_ae339606(bearPower, bbm, bbp, bullPower, BBPower_Color, VIP, VIP_VIM, VIM)

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


