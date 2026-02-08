//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Vortex_Indicator
// ID_model: UBER_1Min_2BV0_9e19bc64 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_UBER_1Min_2BV0_9e19bc64", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_UBER_1Min_9e19bc64(bbp, bullPower, BBPower_Color, bearPower, bbm, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.5,min_samples_leaf=4, random_state=843828734)
	if( bearPower <= 0.068644 )
		if( VIP <= 1.5272 )
			if( bbm <= 0.008615 )
				if( bullPower <= -0.108454 )
					if( VIP_VIM <= -1.14779 )
						if( VIM <= 1.95862 )
							if( bbm <= 9e-05 )
								ret := -1.000000 // sell
							if( bbm > 9e-05 )
								ret := -0.750000 // sell
						if( VIM > 1.95862 )
							if( bearPower <= -0.156398 )
								ret := 0.772727 // buy
							if( bearPower > -0.156398 )
								ret := -0.368421
					if( VIP_VIM > -1.14779 )
						if( bearPower <= -0.191773 )
							if( VIP <= 1.38133 )
								ret := 0.873874 // buy
							if( VIP > 1.38133 )
								ret := 0.000000
						if( bearPower > -0.191773 )
							if( VIP <= 0.748948 )
								ret := -0.416667
							if( VIP > 0.748948 )
								ret := 0.493056
				if( bullPower > -0.108454 )
					if( VIM <= 1.03978 )
						if( VIM <= 0.982146 )
							if( VIP <= 1.3315 )
								ret := -0.169231
							if( VIP > 1.3315 )
								ret := 0.379310
						if( VIM > 0.982146 )
							if( VIP <= 1.07063 )
								ret := 0.000000
							if( VIP > 1.07063 )
								ret := 0.700000 // buy
					if( VIM > 1.03978 )
						if( VIP_VIM <= -0.292198 )
							if( VIP_VIM <= -0.360378 )
								ret := -0.022959
							if( VIP_VIM > -0.360378 )
								ret := -0.350877
						if( VIP_VIM > -0.292198 )
							if( bbm <= 0.002438 )
								ret := 0.031546
							if( bbm > 0.002438 )
								ret := 0.333333
			if( bbm > 0.008615 )
				if( VIM <= 0.757174 )
					if( bullPower <= 0.298352 )
						if( VIP_VIM <= 0.507599 )
							if( bullPower <= 0.109687 )
								ret := 0.062500
							if( bullPower > 0.109687 )
								ret := 0.450276
						if( VIP_VIM > 0.507599 )
							if( VIM <= 0.623116 )
								ret := -0.176744
							if( VIM > 0.623116 )
								ret := 0.084901
					if( bullPower > 0.298352 )
						if( bbp <= 0.63452 )
							if( VIP_VIM <= 0.386531 )
								ret := -0.230769
							if( VIP_VIM > 0.386531 )
								ret := -0.847458 // sell
						if( bbp > 0.63452 )
							if( bbm <= 1.2653 )
								ret := 0.866667 // buy
							if( bbm > 1.2653 )
								ret := -0.148148
				if( VIM > 0.757174 )
					if( VIP <= 1.25906 )
						if( bbp <= 0.261122 )
							if( VIP_VIM <= -0.832365 )
								ret := -0.219873
							if( VIP_VIM > -0.832365 )
								ret := -0.008418
						if( bbp > 0.261122 )
							if( bbm <= 0.221501 )
								ret := 0.489879
							if( bbm > 0.221501 )
								ret := 0.110778
					if( VIP > 1.25906 )
						if( bullPower <= 0.009848 )
							if( bullPower <= -0.243181 )
								ret := 0.800000 // buy
							if( bullPower > -0.243181 )
								ret := 0.116352
						if( bullPower > 0.009848 )
							if( VIP_VIM <= -0.34657 )
								ret := 0.261538
							if( VIP_VIM > -0.34657 )
								ret := -0.281903
		if( VIP > 1.5272 )
			if( bullPower <= -0.058022 )
				if( bullPower <= -0.152038 )
					if( VIP <= 2.29597 )
						if( VIM <= 1.59504 )
							ret := 1.000000 // buy
						if( VIM > 1.59504 )
							if( bbm <= 0.25564 )
								ret := 0.417391
							if( bbm > 0.25564 )
								ret := -1.000000 // sell
					if( VIP > 2.29597 )
						if( VIP_VIM <= 1.9742 )
							if( VIM <= 5533 )
								ret := 0.734959 // buy
							if( VIM > 5533 )
								ret := -0.500000
						if( VIP_VIM > 1.9742 )
							ret := -0.428571
				if( bullPower > -0.152038 )
					if( VIM <= 2.46323 )
						if( VIP_VIM <= -0.092262 )
							if( bbp <= -0.398133 )
								ret := -0.111111
							if( bbp > -0.398133 )
								ret := 0.788043 // buy
						if( VIP_VIM > -0.092262 )
							if( VIP_VIM <= 0.028257 )
								ret := -0.548387
							if( VIP_VIM > 0.028257 )
								ret := 0.570988
					if( VIM > 2.46323 )
						if( VIP <= 1.9333 )
							if( VIP_VIM <= -0.80752 )
								ret := 0.666667
							if( VIP_VIM > -0.80752 )
								ret := -0.970588 // sell
						if( VIP > 1.9333 )
							if( VIP <= 8.4719 )
								ret := 0.326021
							if( VIP > 8.4719 )
								ret := 0.521809
			if( bullPower > -0.058022 )
				if( bullPower <= 0.023254 )
					if( VIP_VIM <= -0.299672 )
						if( VIP_VIM <= -2.31279 )
							if( bbm <= 0.000302 )
								ret := -0.552632
							if( bbm > 0.000302 )
								ret := 0.222222
						if( VIP_VIM > -2.31279 )
							if( VIP <= 19.2031 )
								ret := 0.031662
							if( VIP > 19.2031 )
								ret := 0.380282
					if( VIP_VIM > -0.299672 )
						if( VIP_VIM <= 0.213533 )
							if( bullPower <= -0.004988 )
								ret := 0.398289
							if( bullPower > -0.004988 )
								ret := 0.133758
						if( VIP_VIM > 0.213533 )
							if( VIM <= 10.0301 )
								ret := 0.066191
							if( VIM > 10.0301 )
								ret := 0.293706
				if( bullPower > 0.023254 )
					if( VIP_VIM <= -1.20368 )
						if( VIM <= 4.70468 )
							if( VIP <= 2.2881 )
								ret := 0.625000
							if( VIP > 2.2881 )
								ret := -0.363636
						if( VIM > 4.70468 )
							if( VIP <= 16.1791 )
								ret := -0.691667
							if( VIP > 16.1791 )
								ret := -0.160714
					if( VIP_VIM > -1.20368 )
						if( VIP_VIM <= -0.564991 )
							if( bearPower <= -0.232194 )
								ret := -1.000000 // sell
							if( bearPower > -0.232194 )
								ret := 0.200461
						if( VIP_VIM > -0.564991 )
							if( VIP_VIM <= 0.458064 )
								ret := -0.134743
							if( VIP_VIM > 0.458064 )
								ret := 0.022571
	if( bearPower > 0.068644 )
		if( bbm <= 0.008746 )
			if( bullPower <= 0.086657 )
				if( VIM <= 114.659 )
					if( VIP_VIM <= -1.00215 )
						if( VIM <= 4.8566 )
							ret := 0.000000
						if( VIM > 4.8566 )
							if( VIM <= 6.37924 )
								ret := -0.545455
							if( VIM > 6.37924 )
								ret := -0.815789 // sell
					if( VIP_VIM > -1.00215 )
						if( VIM <= 0.905805 )
							if( VIP <= 1.34878 )
								ret := -1.000000 // sell
							if( VIP > 1.34878 )
								ret := 0.285714
						if( VIM > 0.905805 )
							if( VIM <= 0.988087 )
								ret := 0.750000 // buy
							if( VIM > 0.988087 )
								ret := -0.178808
				if( VIM > 114.659 )
					if( VIM <= 126.1 )
						ret := 1.000000 // buy
					if( VIM > 126.1 )
						ret := 0.750000 // buy
			if( bullPower > 0.086657 )
				if( VIM <= 11.6932 )
					if( VIP_VIM <= 0.234736 )
						if( VIM <= 2.54378 )
							if( VIP <= 2.45953 )
								ret := -0.728767 // sell
							if( VIP > 2.45953 )
								ret := 0.428571
						if( VIM > 2.54378 )
							if( VIM <= 2.70529 )
								ret := 0.257143
							if( VIM > 2.70529 )
								ret := -0.498840
					if( VIP_VIM > 0.234736 )
						if( bbp <= 1.21895 )
							if( VIP <= 1.3665 )
								ret := -0.720588 // sell
							if( VIP > 1.3665 )
								ret := -0.316914
						if( bbp > 1.21895 )
							if( bullPower <= 0.661548 )
								ret := 1.000000 // buy
							if( bullPower > 0.661548 )
								ret := 0.777778 // buy
				if( VIM > 11.6932 )
					if( VIP <= 17.3873 )
						if( bbp <= 0.224041 )
							if( bbm <= 0.000152 )
								ret := -0.192308
							if( bbm > 0.000152 )
								ret := -0.818182 // sell
						if( bbp > 0.224041 )
							if( VIP_VIM <= -0.144418 )
								ret := -0.142857
							if( VIP_VIM > -0.144418 )
								ret := 0.571429
					if( VIP > 17.3873 )
						if( VIP <= 665.434 )
							if( VIP_VIM <= -0.400109 )
								ret := -0.621359
							if( VIP_VIM > -0.400109 )
								ret := -0.221865
						if( VIP > 665.434 )
							ret := 1.000000 // buy
		if( bbm > 0.008746 )
			if( VIM <= 0.896404 )
				if( bearPower <= 0.15511 )
					if( VIP <= 1.50103 )
						if( bullPower <= 0.807518 )
							if( VIM <= 0.727753 )
								ret := -0.007874
							if( VIM > 0.727753 )
								ret := -0.138610
						if( bullPower > 0.807518 )
							ret := 1.000000 // buy
					if( VIP > 1.50103 )
						if( VIM <= 0.723173 )
							if( VIP <= 1.68621 )
								ret := 0.641667
							if( VIP > 1.68621 )
								ret := -0.210526
						if( VIM > 0.723173 )
							if( bullPower <= 0.152749 )
								ret := -0.647059
							if( bullPower > 0.152749 )
								ret := 0.000000
				if( bearPower > 0.15511 )
					if( bbm <= 0.230349 )
						if( bearPower <= 0.454349 )
							if( VIP_VIM <= 0.779405 )
								ret := -0.138384
							if( VIP_VIM > 0.779405 )
								ret := -0.441247
						if( bearPower > 0.454349 )
							if( VIM <= 0.687203 )
								ret := 0.300000
							if( VIM > 0.687203 )
								ret := 0.950000 // buy
					if( bbm > 0.230349 )
						if( bearPower <= 0.657369 )
							if( bullPower <= 0.612909 )
								ret := -0.627119
							if( bullPower > 0.612909 )
								ret := -0.259574
						if( bearPower > 0.657369 )
							if( bullPower <= 2.32512 )
								ret := -1.000000 // sell
							if( bullPower > 2.32512 )
								ret := -0.933333 // sell
			if( VIM > 0.896404 )
				if( VIP_VIM <= -0.166928 )
					if( VIM <= 2.27215 )
						if( VIM <= 1.46084 )
							if( VIP_VIM <= -0.2165 )
								ret := 0.500000
							if( VIP_VIM > -0.2165 )
								ret := -0.666667
						if( VIM > 1.46084 )
							if( VIP_VIM <= -0.388447 )
								ret := -1.000000 // sell
							if( VIP_VIM > -0.388447 )
								ret := -0.928571 // sell
					if( VIM > 2.27215 )
						if( bearPower <= 0.08214 )
							if( bbp <= 0.170828 )
								ret := 0.083333
							if( bbp > 0.170828 )
								ret := 0.928571 // buy
						if( bearPower > 0.08214 )
							if( VIP_VIM <= -1.23167 )
								ret := -0.894737 // sell
							if( VIP_VIM > -1.23167 )
								ret := -0.131148
				if( VIP_VIM > -0.166928 )
					if( VIP <= 2.47805 )
						if( bullPower <= 0.494771 )
							if( VIP_VIM <= 0.726414 )
								ret := 0.059668
							if( VIP_VIM > 0.726414 )
								ret := 0.407143
						if( bullPower > 0.494771 )
							if( VIP_VIM <= 0.425299 )
								ret := 0.888889 // buy
							if( VIP_VIM > 0.425299 )
								ret := 0.050000
					if( VIP > 2.47805 )
						if( bearPower <= 0.164178 )
							if( bearPower <= 0.139966 )
								ret := -0.067797
							if( bearPower > 0.139966 )
								ret := 0.305085
						if( bearPower > 0.164178 )
							if( bearPower <= 0.470681 )
								ret := -0.340517
							if( bearPower > 0.470681 )
								ret := 0.571429
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_UBER_1Min_9e19bc64(bbp, bullPower, BBPower_Color, bearPower, bbm, VIP, VIP_VIM, VIM)

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


