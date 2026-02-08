//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: AMZN_30Min_2BT0_fae60b62 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AMZN_30Min_2BT0_fae60b62", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AMZN_30Min_fae60b62(bullPower, bbp, bearPower, bbm, BBPower_Color, ema3, tema, ema2, ema12, ema13, ema1)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( tema <= 3143.17 )
		if( tema <= 82.9336 )
			if( ema1 <= 82.4335 )
				ret := 0.615385
			if( ema1 > 82.4335 )
				if( ema3 <= 83.6579 )
					ret := 1.000000 // buy
				if( ema3 > 83.6579 )
					if( ema1 <= 321.858 )
						if( ema13 <= -1.85204 )
							ret := 0.812500 // buy
						if( ema13 > -1.85204 )
							ret := 0.454545
					if( ema1 > 321.858 )
						ret := 1.000000 // buy
		if( tema > 82.9336 )
			if( bbm <= 10.4229 )
				if( ema12 <= 23.0908 )
					if( tema <= 2647.24 )
						if( ema13 <= 2.46194 )
							if( bullPower <= 1.57782 )
								if( ema2 <= 83.6346 )
									ret := 0.694118
								if( ema2 > 83.6346 )
									ret := 0.016520
							if( bullPower > 1.57782 )
								if( ema13 <= -1.19857 )
									ret := 0.066800
								if( ema13 > -1.19857 )
									ret := -0.107639
						if( ema13 > 2.46194 )
							if( ema12 <= 14.0093 )
								if( bullPower <= -0.282469 )
									ret := 0.315000
								if( bullPower > -0.282469 )
									ret := 0.092987
							if( ema12 > 14.0093 )
								if( ema1 <= 1916.57 )
									ret := -0.013514
								if( ema1 > 1916.57 )
									ret := -0.614865
					if( tema > 2647.24 )
						if( ema3 <= 2932.15 )
							if( tema <= 2867.94 )
								if( ema2 <= 2804.2 )
									ret := 0.537367
								if( ema2 > 2804.2 )
									ret := -0.359551
							if( tema > 2867.94 )
								if( bullPower <= 7.14047 )
									ret := 0.405405
								if( bullPower > 7.14047 )
									ret := 0.886598 // buy
						if( ema3 > 2932.15 )
							if( bbp <= 10.0212 )
								if( ema13 <= -16.7084 )
									ret := -0.094718
								if( ema13 > -16.7084 )
									ret := 0.473236
							if( bbp > 10.0212 )
								if( bbm <= 7.86318 )
									ret := -0.290000
								if( bbm > 7.86318 )
									ret := 0.257576
				if( ema12 > 23.0908 )
					if( ema1 <= 2998.77 )
						if( ema3 <= 1758.46 )
							ret := -0.294118
						if( ema3 > 1758.46 )
							if( ema1 <= 2896.05 )
								if( bbm <= 6.88286 )
									ret := -0.981818 // sell
								if( bbm > 6.88286 )
									ret := -0.826087 // sell
							if( ema1 > 2896.05 )
								ret := -0.562500
					if( ema1 > 2998.77 )
						ret := -0.222222
			if( bbm > 10.4229 )
				if( ema12 <= -2.06722 )
					if( tema <= 2797.55 )
						if( ema3 <= 2781.81 )
							if( bbm <= 10.4995 )
								if( bullPower <= -1.20582 )
									ret := -0.826087 // sell
								if( bullPower > -1.20582 )
									ret := -0.454545
							if( bbm > 10.4995 )
								if( ema1 <= 2459.63 )
									ret := -0.051250
								if( ema1 > 2459.63 )
									ret := -0.543478
						if( ema3 > 2781.81 )
							if( bbm <= 19.5039 )
								if( ema2 <= 2826.97 )
									ret := 0.000000
								if( ema2 > 2826.97 )
									ret := -0.818182 // sell
							if( bbm > 19.5039 )
								if( ema1 <= 2811.65 )
									ret := 0.906667 // buy
								if( ema1 > 2811.65 )
									ret := 0.190476
					if( tema > 2797.55 )
						if( ema12 <= -5.10043 )
							if( ema2 <= 3157.98 )
								if( tema <= 2865.23 )
									ret := -0.815534 // sell
								if( tema > 2865.23 )
									ret := -0.337556
							if( ema2 > 3157.98 )
								if( ema13 <= -27.7713 )
									ret := 0.836735 // buy
								if( ema13 > -27.7713 )
									ret := -0.145833
						if( ema12 > -5.10043 )
							if( bullPower <= 2.61595 )
								if( tema <= 3068.58 )
									ret := -0.462687
								if( tema > 3068.58 )
									ret := 0.159091
							if( bullPower > 2.61595 )
								if( bbp <= 3.41161 )
									ret := 0.598361
								if( bbp > 3.41161 )
									ret := -0.272727
				if( ema12 > -2.06722 )
					if( ema3 <= 2426.24 )
						if( ema1 <= 1425.03 )
							if( ema2 <= 1326.01 )
								if( ema13 <= 3.18522 )
									ret := -0.168317
								if( ema13 > 3.18522 )
									ret := 0.395062
							if( ema2 > 1326.01 )
								if( bbm <= 21.5536 )
									ret := 0.720670 // buy
								if( bbm > 21.5536 )
									ret := -0.076923
						if( ema1 > 1425.03 )
							if( bearPower <= -10.4062 )
								if( bbm <= 71.8287 )
									ret := 0.125523
								if( bbm > 71.8287 )
									ret := -1.000000 // sell
							if( bearPower > -10.4062 )
								if( ema1 <= 2388.27 )
									ret := -0.147535
								if( ema1 > 2388.27 )
									ret := -0.786885 // sell
					if( ema3 > 2426.24 )
						if( ema12 <= 1.96039 )
							if( ema3 <= 3140.47 )
								if( bbp <= -18.6223 )
									ret := -0.142857
								if( bbp > -18.6223 )
									ret := 0.356299
							if( ema3 > 3140.47 )
								ret := -0.647059
						if( ema12 > 1.96039 )
							if( bbm <= 19.8222 )
								if( ema13 <= 6.06976 )
									ret := -0.120370
								if( ema13 > 6.06976 )
									ret := 0.312704
							if( bbm > 19.8222 )
								if( ema12 <= 18.3173 )
									ret := -0.141762
								if( ema12 > 18.3173 )
									ret := 0.302521
	if( tema > 3143.17 )
		if( ema13 <= -38.5883 )
			if( ema2 <= 3374.54 )
				if( ema13 <= -40.4152 )
					if( ema13 <= -43.5402 )
						if( tema <= 3286.1 )
							if( bbp <= -145.176 )
								ret := 1.000000 // buy
							if( bbp > -145.176 )
								if( bbp <= -91.048 )
									ret := 0.100000
								if( bbp > -91.048 )
									ret := 0.783333 // buy
						if( tema > 3286.1 )
							ret := 1.000000 // buy
					if( ema13 > -43.5402 )
						if( ema3 <= 3317.22 )
							if( ema1 <= 3233.75 )
								ret := 0.571429
							if( ema1 > 3233.75 )
								ret := -0.166667
						if( ema3 > 3317.22 )
							ret := 0.904762 // buy
				if( ema13 > -40.4152 )
					if( bearPower <= -36.9064 )
						ret := 0.500000
					if( bearPower > -36.9064 )
						ret := -0.538462
			if( ema2 > 3374.54 )
				if( ema3 <= 3657.87 )
					if( ema3 <= 3411.84 )
						ret := 0.388889
					if( ema3 > 3411.84 )
						if( ema1 <= 3402.35 )
							if( bbp <= -44.5752 )
								if( bullPower <= -41.9023 )
									ret := -0.695652
								if( bullPower > -41.9023 )
									ret := -0.250000
							if( bbp > -44.5752 )
								ret := -1.000000 // sell
						if( ema1 > 3402.35 )
							if( bbm <= 21.0283 )
								ret := 0.176471
							if( bbm > 21.0283 )
								ret := -0.500000
				if( ema3 > 3657.87 )
					if( bearPower <= -57.4605 )
						ret := 0.384615
					if( bearPower > -57.4605 )
						ret := 1.000000 // buy
		if( ema13 > -38.5883 )
			if( ema13 <= -11.4782 )
				if( bbm <= 0.115567 )
					if( ema3 <= 3507.32 )
						if( tema <= 3270.72 )
							if( bullPower <= -15.6499 )
								if( ema2 <= 3179.17 )
									ret := 0.888889 // buy
								if( ema2 > 3179.17 )
									ret := 1.000000 // buy
							if( bullPower > -15.6499 )
								if( tema <= 3180.73 )
									ret := 0.090909
								if( tema > 3180.73 )
									ret := -0.333333
						if( tema > 3270.72 )
							if( tema <= 3292.1 )
								if( bearPower <= -6.79952 )
									ret := -0.363636
								if( bearPower > -6.79952 )
									ret := -0.800000 // sell
							if( tema > 3292.1 )
								if( ema12 <= -10.8726 )
									ret := -0.250000
								if( ema12 > -10.8726 )
									ret := 0.071429
					if( ema3 > 3507.32 )
						if( bearPower <= -8.34268 )
							if( ema2 <= 3505.26 )
								ret := 1.000000 // buy
							if( ema2 > 3505.26 )
								ret := 0.444444
						if( bearPower > -8.34268 )
							ret := 0.307692
				if( bbm > 0.115567 )
					if( ema13 <= -19.6134 )
						if( ema1 <= 3354.64 )
							if( ema1 <= 3292.47 )
								if( tema <= 3208.23 )
									ret := 0.144144
								if( tema > 3208.23 )
									ret := -0.492537
							if( ema1 > 3292.47 )
								if( ema2 <= 3367.11 )
									ret := 0.226804
								if( ema2 > 3367.11 )
									ret := 1.000000 // buy
						if( ema1 > 3354.64 )
							if( tema <= 3412.05 )
								if( bbm <= 5.26575 )
									ret := -0.957447 // sell
								if( bbm > 5.26575 )
									ret := -0.500000
							if( tema > 3412.05 )
								if( ema12 <= -13.5121 )
									ret := -0.372671
								if( ema12 > -13.5121 )
									ret := 0.136842
					if( ema13 > -19.6134 )
						if( ema12 <= -8.42714 )
							if( ema2 <= 3509.32 )
								if( bbm <= 8.48 )
									ret := 0.173913
								if( bbm > 8.48 )
									ret := -0.480769
							if( ema2 > 3509.32 )
								if( ema13 <= -14.7944 )
									ret := -0.964706 // sell
								if( ema13 > -14.7944 )
									ret := -0.636364
						if( ema12 > -8.42714 )
							if( bbp <= 13.2397 )
								if( ema1 <= 3470.4 )
									ret := -0.308394
								if( ema1 > 3470.4 )
									ret := 0.709677 // buy
							if( bbp > 13.2397 )
								if( ema13 <= -14.9219 )
									ret := -0.357143
								if( ema13 > -14.9219 )
									ret := -0.937500 // sell
			if( ema13 > -11.4782 )
				if( ema1 <= 3180.3 )
					if( ema12 <= -6.77732 )
						if( bbm <= 11.1457 )
							ret := -0.076923
						if( bbm > 11.1457 )
							if( ema12 <= -7.23435 )
								ret := 0.480000
							if( ema12 > -7.23435 )
								ret := 0.866667 // buy
					if( ema12 > -6.77732 )
						if( tema <= 3178.84 )
							if( ema12 <= 38.4267 )
								if( bbm <= 24.0872 )
									ret := -0.129244
								if( bbm > 24.0872 )
									ret := -0.574324
							if( ema12 > 38.4267 )
								ret := 0.750000 // buy
						if( tema > 3178.84 )
							if( ema12 <= 12.5505 )
								if( bearPower <= 2.2079 )
									ret := -0.888889 // sell
								if( bearPower > 2.2079 )
									ret := -0.427350
							if( ema12 > 12.5505 )
								if( ema3 <= 3140.93 )
									ret := -0.510417
								if( ema3 > 3140.93 )
									ret := 0.192982
				if( ema1 > 3180.3 )
					if( tema <= 3293.45 )
						if( bbp <= -58.3698 )
							if( bbp <= -70.9625 )
								ret := 0.222222
							if( bbp > -70.9625 )
								ret := -1.000000 // sell
						if( bbp > -58.3698 )
							if( ema1 <= 3296.02 )
								if( ema2 <= 3204.58 )
									ret := 0.191532
								if( ema2 > 3204.58 )
									ret := -0.011075
							if( ema1 > 3296.02 )
								if( ema12 <= -4.32192 )
									ret := 0.847826 // buy
								if( ema12 > -4.32192 )
									ret := 0.000000
					if( tema > 3293.45 )
						if( tema <= 3738.36 )
							if( tema <= 3308.64 )
								if( ema3 <= 3302.69 )
									ret := -0.116438
								if( ema3 > 3302.69 )
									ret := -0.513514
							if( tema > 3308.64 )
								if( ema13 <= -6.97707 )
									ret := 0.151079
								if( ema13 > -6.97707 )
									ret := -0.078040
						if( tema > 3738.36 )
							if( ema13 <= 23.8213 )
								ret := -1.000000 // sell
							if( ema13 > 23.8213 )
								ret := -0.750000 // sell
	
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


//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


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
float op_operation = decision_tree_0_AMZN_30Min_fae60b62(bullPower, bbp, bearPower, bbm, BBPower_Color, ema3, tema, ema2, ema12, ema13, ema1)

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


