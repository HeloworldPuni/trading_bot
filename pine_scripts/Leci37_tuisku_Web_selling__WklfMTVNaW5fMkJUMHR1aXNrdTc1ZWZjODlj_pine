//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: ZI_15Min_2BT0_75efc89c Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ZI_15Min_2BT0_75efc89c", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ZI_15Min_75efc89c(bbp, bullPower, BBPower_Color, bearPower, bbm, ema2, tema, ema12, ema3, ema1, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( bearPower <= 0.107101 )
		if( bbm <= 0.000114 )
			if( bearPower <= -0.248408 )
				if( ema13 <= -0.213203 )
					if( ema12 <= -0.722425 )
						ret := -0.900000 // sell
					if( ema12 > -0.722425 )
						if( bearPower <= -0.50322 )
							ret := 0.470833
						if( bearPower > -0.50322 )
							ret := 0.150602
				if( ema13 > -0.213203 )
					if( ema1 <= 54.1873 )
						if( tema <= 42.1963 )
							ret := 0.522727
						if( tema > 42.1963 )
							ret := 0.807692 // buy
					if( ema1 > 54.1873 )
						if( ema1 <= 66.41 )
							ret := -0.040000
						if( ema1 > 66.41 )
							ret := 0.800000 // buy
			if( bearPower > -0.248408 )
				if( tema <= 47.7166 )
					if( bullPower <= 0.044236 )
						if( bullPower <= -0.244185 )
							ret := -0.846154 // sell
						if( bullPower > -0.244185 )
							ret := 0.221683
					if( bullPower > 0.044236 )
						if( ema3 <= 42.985 )
							ret := -0.216102
						if( ema3 > 42.985 )
							ret := 0.285714
				if( tema > 47.7166 )
					if( bearPower <= 0.006224 )
						if( bearPower <= -0.120407 )
							ret := -0.038462
						if( bearPower > -0.120407 )
							ret := -0.492537
					if( bearPower > 0.006224 )
						if( ema2 <= 64.534 )
							ret := 0.241758
						if( ema2 > 64.534 )
							ret := -0.225000
		if( bbm > 0.000114 )
			if( bearPower <= -1.30924 )
				if( ema1 <= 49.8591 )
					if( ema3 <= 48.5233 )
						if( ema2 <= 29.3935 )
							ret := 0.882353 // buy
						if( ema2 > 29.3935 )
							ret := 0.212727
					if( ema3 > 48.5233 )
						if( bullPower <= -0.822468 )
							ret := 0.810606 // buy
						if( bullPower > -0.822468 )
							ret := 0.304348
				if( ema1 > 49.8591 )
					if( ema1 <= 51.4706 )
						if( ema3 <= 50.3294 )
							ret := 1.000000 // buy
						if( ema3 > 50.3294 )
							ret := -0.617647
					if( ema1 > 51.4706 )
						if( bullPower <= -1.408 )
							ret := -0.549550
						if( bullPower > -1.408 )
							ret := 0.268657
			if( bearPower > -1.30924 )
				if( ema3 <= 8.81957 )
					if( ema12 <= 0.036985 )
						if( ema13 <= -0.11974 )
							ret := -0.195122
						if( ema13 > -0.11974 )
							ret := 0.805556 // buy
					if( ema12 > 0.036985 )
						if( bbm <= 0.124681 )
							ret := 0.684211
						if( bbm > 0.124681 )
							ret := -0.628571
				if( ema3 > 8.81957 )
					if( ema13 <= -0.336984 )
						if( tema <= 13.756 )
							ret := -0.769231 // sell
						if( tema > 13.756 )
							ret := -0.034584
					if( ema13 > -0.336984 )
						if( bullPower <= -0.2012 )
							ret := 0.191166
						if( bullPower > -0.2012 )
							ret := 0.012077
	if( bearPower > 0.107101 )
		if( ema2 <= 71.5474 )
			if( bbm <= 0.109912 )
				if( bullPower <= 0.555572 )
					if( ema2 <= 27.3177 )
						if( bearPower <= 0.261121 )
							ret := -0.265440
						if( bearPower > 0.261121 )
							ret := -0.705882 // sell
					if( ema2 > 27.3177 )
						if( ema1 <= 42.7224 )
							ret := 0.040706
						if( ema1 > 42.7224 )
							ret := -0.208676
				if( bullPower > 0.555572 )
					if( ema12 <= 0.265598 )
						if( ema3 <= 40.8397 )
							ret := -0.484375
						if( ema3 > 40.8397 )
							ret := -0.745665 // sell
					if( ema12 > 0.265598 )
						if( ema12 <= 0.267575 )
							ret := 1.000000 // buy
						if( ema12 > 0.267575 )
							ret := -0.486154
			if( bbm > 0.109912 )
				if( ema2 <= 29.1839 )
					if( ema3 <= 22.3236 )
						if( ema12 <= 0.2799 )
							ret := -0.230159
						if( ema12 > 0.2799 )
							ret := 0.307692
					if( ema3 > 22.3236 )
						if( ema1 <= 29.1939 )
							ret := 0.262590
						if( ema1 > 29.1939 )
							ret := 0.913793 // buy
				if( ema2 > 29.1839 )
					if( tema <= 34.1834 )
						if( ema3 <= 32.6199 )
							ret := -0.334375
						if( ema3 > 32.6199 )
							ret := -0.924242 // sell
					if( tema > 34.1834 )
						if( tema <= 36.1489 )
							ret := 0.500000
						if( tema > 36.1489 )
							ret := -0.054857
		if( ema2 > 71.5474 )
			if( ema13 <= 0.463237 )
				if( ema2 <= 73.5118 )
					if( BBPower_Color <= 0.5 )
						ret := 1.000000 // buy
					if( BBPower_Color > 0.5 )
						if( bbp <= 0.645123 )
							ret := 0.111111
						if( bbp > 0.645123 )
							ret := 0.000000
				if( ema2 > 73.5118 )
					if( bbm <= 0.14515 )
						if( tema <= 74.3342 )
							ret := -1.000000 // sell
						if( tema > 74.3342 )
							ret := -0.615385
					if( bbm > 0.14515 )
						if( tema <= 77.2312 )
							ret := -0.055556
						if( tema > 77.2312 )
							ret := -1.000000 // sell
			if( ema13 > 0.463237 )
				if( ema1 <= 75.9937 )
					if( bbp <= 1.89545 )
						if( bullPower <= 1.00088 )
							ret := -1.000000 // sell
						if( bullPower > 1.00088 )
							ret := -0.833333 // sell
					if( bbp > 1.89545 )
						ret := 0.000000
				if( ema1 > 75.9937 )
					if( ema2 <= 77.7844 )
						ret := 0.000000
					if( ema2 > 77.7844 )
						ret := -0.857143 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_ZI_15Min_75efc89c(bbp, bullPower, BBPower_Color, bearPower, bbm, ema2, tema, ema12, ema3, ema1, ema13)

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


