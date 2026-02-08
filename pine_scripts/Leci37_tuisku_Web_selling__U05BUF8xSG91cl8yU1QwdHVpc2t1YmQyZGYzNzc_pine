//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: SNAP_1Hour_2ST0_bd2df377 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Hour_2ST0_bd2df377", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Hour_bd2df377(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( ema3 <= 10.4045 )
		if( smoothD_d <= 95.6047 )
			if( rsi1 <= 26.1162 )
				if( ema12 <= -0.595038 )
					ret := -1.000000 // sell
				if( ema12 > -0.595038 )
					if( tema <= 10.0037 )
						if( k <= 1.65163 )
							ret := 0.660000
						if( k > 1.65163 )
							ret := 0.325077
					if( tema > 10.0037 )
						if( rsi1 <= 16.8333 )
							ret := -1.000000 // sell
						if( rsi1 > 16.8333 )
							ret := -0.225806
			if( rsi1 > 26.1162 )
				if( smoothD_d <= 7.38578 )
					if( rsi1 <= 33.725 )
						if( ema12 <= -0.201052 )
							ret := -0.823529 // sell
						if( ema12 > -0.201052 )
							ret := 0.152174
					if( rsi1 > 33.725 )
						if( smoothK_k <= -0.60903 )
							ret := -0.635714
						if( smoothK_k > -0.60903 )
							ret := -0.243902
				if( smoothD_d > 7.38578 )
					if( rsi1 <= 70.8123 )
						if( smoothD_d <= 88.5849 )
							ret := 0.140505
						if( smoothD_d > 88.5849 )
							ret := -0.150685
					if( rsi1 > 70.8123 )
						if( d <= 90.3722 )
							ret := 0.134298
						if( d > 90.3722 )
							ret := 0.429975
		if( smoothD_d > 95.6047 )
			if( rsi1 <= 73.6171 )
				if( k <= 97.6044 )
					ret := 0.000000
				if( k > 97.6044 )
					if( ema13 <= 0.010741 )
						if( ema1 <= 8.73728 )
							ret := -0.857143 // sell
						if( ema1 > 8.73728 )
							ret := -1.000000 // sell
					if( ema13 > 0.010741 )
						if( ema13 <= 0.080689 )
							ret := -0.133333
						if( ema13 > 0.080689 )
							ret := -0.882353 // sell
			if( rsi1 > 73.6171 )
				if( ema3 <= 9.63347 )
					if( rsi1 <= 94.2637 )
						if( ema2 <= 9.61343 )
							ret := -0.074074
						if( ema2 > 9.61343 )
							ret := -1.000000 // sell
					if( rsi1 > 94.2637 )
						ret := -0.916667 // sell
				if( ema3 > 9.63347 )
					if( smoothD_d <= 96.8031 )
						if( smoothD_d <= 95.8556 )
							ret := 0.000000
						if( smoothD_d > 95.8556 )
							ret := 0.885714 // buy
					if( smoothD_d > 96.8031 )
						ret := -0.333333
	if( ema3 > 10.4045 )
		if( d_k <= 18.7675 )
			if( rsi1 <= 20.1672 )
				if( ema3 <= 11.6278 )
					if( smoothD_d <= -2.31182 )
						if( d <= 0.107038 )
							ret := 0.000000
						if( d > 0.107038 )
							ret := 0.947368 // buy
					if( smoothD_d > -2.31182 )
						if( ema12 <= -0.270276 )
							ret := 0.555556
						if( ema12 > -0.270276 )
							ret := -0.081633
				if( ema3 > 11.6278 )
					if( ema12 <= -0.950865 )
						if( ema13 <= -2.99805 )
							ret := -0.746667 // sell
						if( ema13 > -2.99805 )
							ret := 0.236486
					if( ema12 > -0.950865 )
						if( ema3 <= 33.3189 )
							ret := -0.353147
						if( ema3 > 33.3189 )
							ret := -0.708333 // sell
			if( rsi1 > 20.1672 )
				if( rsi1 <= 86.362 )
					if( ema12 <= 0.470378 )
						if( smoothD_d <= 95.822 )
							ret := -0.026062
						if( smoothD_d > 95.822 )
							ret := -0.322289
					if( ema12 > 0.470378 )
						if( ema2 <= 58.5266 )
							ret := 0.266106
						if( ema2 > 58.5266 )
							ret := -0.068111
				if( rsi1 > 86.362 )
					if( ema2 <= 11.3206 )
						if( ema12 <= 0.115564 )
							ret := -0.277778
						if( ema12 > 0.115564 )
							ret := -0.851064 // sell
					if( ema2 > 11.3206 )
						if( ema13 <= 1.94474 )
							ret := -0.176647
						if( ema13 > 1.94474 )
							ret := -0.688525
		if( d_k > 18.7675 )
			if( rsi1 <= 36.3917 )
				if( d <= 28.9194 )
					if( ema1 <= 13.9561 )
						if( k <= 0.994807 )
							ret := 0.920000 // buy
						if( k > 0.994807 )
							ret := -0.250000
					if( ema1 > 13.9561 )
						if( ema12 <= -0.244118 )
							ret := -0.888889 // sell
						if( ema12 > -0.244118 )
							ret := -0.210526
				if( d > 28.9194 )
					if( tema <= 15.2627 )
						if( smoothD_d <= 64.6368 )
							ret := 0.358025
						if( smoothD_d > 64.6368 )
							ret := -0.347826
					if( tema > 15.2627 )
						if( d_k <= 30.6969 )
							ret := 0.670213
						if( d_k > 30.6969 )
							ret := 0.047619
			if( rsi1 > 36.3917 )
				if( ema13 <= 0.069029 )
					if( d <= 24.0057 )
						ret := 1.000000 // buy
					if( d > 24.0057 )
						if( ema3 <= 67.0661 )
							ret := -0.233945
						if( ema3 > 67.0661 )
							ret := 0.541667
				if( ema13 > 0.069029 )
					if( rsi1 <= 75.8965 )
						if( ema1 <= 15.1737 )
							ret := 0.428571
						if( ema1 > 15.1737 )
							ret := 0.031175
					if( rsi1 > 75.8965 )
						if( smoothD_d <= 76.9293 )
							ret := -0.769231 // sell
						if( smoothD_d > 76.9293 )
							ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Stochastic_RSI 
//@version=5
//indicator title="Stochastic RSI", shorttitle="Stoch RSI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
smoothK = input.int(3, "K", minval=1)
smoothD = input.int(3, "D", minval=1)
lengthRSI = input.int(14, "RSI Length", minval=1)
lengthStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)
plot(k, "K", color=#2962FF)
plot(d, "D", color=#FF6D00)

d_k = d - k
smoothD_d = d - smoothD
smoothK_k = k - smoothK

h0 = hline(80, "Upper Band", color=#787B86)
hline(50, "Middle Band", color=color.new(#787B86, 50))
h1 = hline(20, "Lower Band", color=#787B86)
fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")

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
float op_operation = decision_tree_0_SNAP_1Hour_bd2df377(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)

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


