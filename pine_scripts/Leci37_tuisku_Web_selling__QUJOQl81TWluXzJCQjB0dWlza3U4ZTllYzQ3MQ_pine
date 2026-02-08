//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bollinger_Bands, L_Bull_Bear_Power
// ID_model: ABNB_5Min_2BB0_8e9ec471 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ABNB_5Min_2BB0_8e9ec471", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ABNB_5Min_8e9ec471(Upper_Band, basis, Lower_Band, bullPower, bbp, bearPower, bbm, BBPower_Color)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( bullPower <= -0.129484 )
		if( basis <= 148.828 )
			if( Upper_Band <= 143.364 )
				if( bbm <= 0.248565 )
					if( bbp <= -1.2613 )
						if( Lower_Band <= 114.05 )
							ret := -0.318182
						if( Lower_Band > 114.05 )
							ret := 0.517677
					if( bbp > -1.2613 )
						if( Lower_Band <= 137.706 )
							ret := 0.105317
						if( Lower_Band > 137.706 )
							ret := 0.355353
				if( bbm > 0.248565 )
					if( basis <= 137.914 )
						if( Upper_Band <= 113.852 )
							ret := -0.200549
						if( Upper_Band > 113.852 )
							ret := 0.120731
					if( basis > 137.914 )
						if( bearPower <= -1.51352 )
							ret := 1.000000 // buy
						if( bearPower > -1.51352 )
							ret := -0.318966
			if( Upper_Band > 143.364 )
				if( basis <= 143.085 )
					if( bbm <= 0.015737 )
						if( basis <= 142.652 )
							ret := -0.500000
						if( basis > 142.652 )
							ret := 0.166667
					if( bbm > 0.015737 )
						if( basis <= 142.653 )
							ret := 0.512000
						if( basis > 142.653 )
							ret := 0.863636 // buy
				if( basis > 143.085 )
					if( bearPower <= -0.736028 )
						if( basis <= 143.798 )
							ret := -0.550725
						if( basis > 143.798 )
							ret := 0.147107
					if( bearPower > -0.736028 )
						if( bullPower <= -0.350682 )
							ret := 0.611650
						if( bullPower > -0.350682 )
							ret := 0.245720
		if( basis > 148.828 )
			if( bbp <= -2.01067 )
				if( Upper_Band <= 168.257 )
					if( Lower_Band <= 148.062 )
						if( bbm <= 1.53108 )
							ret := -0.500000
						if( bbm > 1.53108 )
							ret := -1.000000 // sell
					if( Lower_Band > 148.062 )
						if( Lower_Band <= 153.461 )
							ret := 0.054054
						if( Lower_Band > 153.461 )
							ret := -0.576642
				if( Upper_Band > 168.257 )
					if( bbp <= -3.77344 )
						ret := 1.000000 // buy
					if( bbp > -3.77344 )
						ret := 0.777778 // buy
			if( bbp > -2.01067 )
				if( bbm <= 0.038778 )
					if( Lower_Band <= 149.906 )
						if( Lower_Band <= 149.634 )
							ret := 0.113636
						if( Lower_Band > 149.634 )
							ret := -0.666667
					if( Lower_Band > 149.906 )
						if( bbp <= -1.49061 )
							ret := 0.787234 // buy
						if( bbp > -1.49061 )
							ret := 0.342391
				if( bbm > 0.038778 )
					if( basis <= 150.31 )
						if( basis <= 150.184 )
							ret := -0.210784
						if( basis > 150.184 )
							ret := -0.975000 // sell
					if( basis > 150.31 )
						if( Lower_Band <= 148.563 )
							ret := 0.925926 // buy
						if( Lower_Band > 148.563 )
							ret := 0.015085
	if( bullPower > -0.129484 )
		if( bullPower <= 1.96538 )
			if( bbp <= 2.30016 )
				if( Lower_Band <= 114.225 )
					if( basis <= 113.565 )
						if( bearPower <= -0.186862 )
							ret := -0.203416
						if( bearPower > -0.186862 )
							ret := 0.071429
					if( basis > 113.565 )
						if( bullPower <= 1.0465 )
							ret := 0.260757
						if( bullPower > 1.0465 )
							ret := -0.420290
				if( Lower_Band > 114.225 )
					if( basis <= 116.061 )
						if( bbm <= 0.564253 )
							ret := -0.297638
						if( bbm > 0.564253 )
							ret := 0.379747
					if( basis > 116.061 )
						if( basis <= 116.945 )
							ret := 0.187940
						if( basis > 116.945 )
							ret := -0.037787
			if( bbp > 2.30016 )
				if( basis <= 158.31 )
					if( Upper_Band <= 118.875 )
						if( Upper_Band <= 113.717 )
							ret := 0.777778 // buy
						if( Upper_Band > 113.717 )
							ret := -0.535714
					if( Upper_Band > 118.875 )
						if( basis <= 130.862 )
							ret := 0.608696
						if( basis > 130.862 )
							ret := 0.183099
				if( basis > 158.31 )
					if( bullPower <= 1.62305 )
						ret := -0.176471
					if( bullPower > 1.62305 )
						if( bbm <= 0.836568 )
							ret := -0.750000 // sell
						if( bbm > 0.836568 )
							ret := -1.000000 // sell
		if( bullPower > 1.96538 )
			if( Upper_Band <= 153.207 )
				if( Lower_Band <= 144.948 )
					if( bearPower <= 2.14538 )
						if( bearPower <= 0.675076 )
							ret := -0.657895
						if( bearPower > 0.675076 )
							ret := -0.253731
					if( bearPower > 2.14538 )
						ret := 0.937500 // buy
				if( Lower_Band > 144.948 )
					if( bullPower <= 2.50491 )
						ret := 0.913043 // buy
					if( bullPower > 2.50491 )
						ret := 0.250000
			if( Upper_Band > 153.207 )
				if( bbp <= 3.12502 )
					if( bearPower <= 0.988525 )
						if( bullPower <= 2.19304 )
							ret := -0.920000 // sell
						if( bullPower > 2.19304 )
							ret := -0.461538
					if( bearPower > 0.988525 )
						ret := 0.538462
				if( bbp > 3.12502 )
					if( Upper_Band <= 162.54 )
						if( Lower_Band <= 149.921 )
							ret := -0.952381 // sell
						if( Lower_Band > 149.921 )
							ret := -1.000000 // sell
					if( Upper_Band > 162.54 )
						ret := -0.600000
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bollinger_Bands 
//@version=5
//indicator shorttitle="BB", title="Bollinger Bands", overlay=true, timeframe="", timeframe_gaps=true)
length_BB = input.int(20, minval=1)
maType = input.string("SMA", "Basis MA Type", options = ["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"])
src = input(close, title="Source")
mult = input.float(2.0, minval=0.001, maxval=50, title="StdDev")

ma(source, length_BB, _type) =>
    switch _type
        "SMA" => ta.sma(source, length_BB)
        "EMA" => ta.ema(source, length_BB)
        "SMMA (RMA)" => ta.rma(source, length_BB)
        "WMA" => ta.wma(source, length_BB)
        "VWMA" => ta.vwma(source, length_BB)

basis = ma(src, length_BB, maType)
dev = mult * ta.stdev(src, length_BB)
Upper_Band = basis + dev
Lower_Band = basis - dev
offset = input.int(0, "Offset", minval = -500, maxval = 500, display = display.data_window)
plot(basis, "Basis", color=#2962FF, offset = offset)
p1 = plot(Upper_Band, "Upper", color=#F23645, offset = offset)
p2 = plot(Lower_Band, "Lower", color=#089981, offset = offset)
fill(p1, p2, title = "Background", color=color.rgb(33, 150, 243, 95))

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
float op_operation = decision_tree_0_ABNB_5Min_8e9ec471(Upper_Band, basis, Lower_Band, bullPower, bbp, bearPower, bbm, BBPower_Color)

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


