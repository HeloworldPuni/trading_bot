//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: SHOP_1Min_2ST0_9fb20c01 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SHOP_1Min_2ST0_9fb20c01", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SHOP_1Min_9fb20c01(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( d <= 94.8675 )
		if( ema12 <= -0.106011 )
			if( d_k <= 23.3314 )
				if( k <= 93.1563 )
					if( ema3 <= 80.974 )
						if( smoothD_d <= -2.92138 )
							if( tema <= 77.9024 )
								if( ema1 <= 70.049 )
									ret := -0.347826
								if( ema1 > 70.049 )
									ret := 0.468750
							if( tema > 77.9024 )
								if( ema12 <= -0.120313 )
									ret := -1.000000 // sell
								if( ema12 > -0.120313 )
									ret := -0.500000
						if( smoothD_d > -2.92138 )
							if( ema13 <= -0.133932 )
								if( d <= 4.26655 )
									ret := 0.267184
								if( d > 4.26655 )
									ret := 0.104560
							if( ema13 > -0.133932 )
								if( rsi1 <= 33.5513 )
									ret := 0.357143
								if( rsi1 > 33.5513 )
									ret := 0.975610 // buy
					if( ema3 > 80.974 )
						if( rsi1 <= 38.7397 )
							if( ema1 <= 83.3398 )
								if( rsi1 <= 29.1817 )
									ret := 0.659574
								if( rsi1 > 29.1817 )
									ret := 0.901961 // buy
							if( ema1 > 83.3398 )
								ret := -0.250000
						if( rsi1 > 38.7397 )
							if( k <= 27.7952 )
								if( ema3 <= 82.3845 )
									ret := 1.000000 // buy
								if( ema3 > 82.3845 )
									ret := 0.000000
							if( k > 27.7952 )
								if( smoothD_d <= 44.0307 )
									ret := -1.000000 // sell
								if( smoothD_d > 44.0307 )
									ret := 1.000000 // buy
				if( k > 93.1563 )
					if( rsi1 <= 56.8693 )
						if( ema2 <= 71.1867 )
							if( tema <= 70.1055 )
								if( rsi1 <= 24.6094 )
									ret := 0.333333
								if( rsi1 > 24.6094 )
									ret := 0.860000 // buy
							if( tema > 70.1055 )
								ret := 0.142857
						if( ema2 > 71.1867 )
							ret := 1.000000 // buy
					if( rsi1 > 56.8693 )
						ret := -1.000000 // sell
			if( d_k > 23.3314 )
				if( ema1 <= 57.1434 )
					ret := 1.000000 // buy
				if( ema1 > 57.1434 )
					if( ema2 <= 65.8762 )
						if( ema1 <= 59.9925 )
							ret := -1.000000 // sell
						if( ema1 > 59.9925 )
							if( tema <= 64.8645 )
								ret := 0.714286 // buy
							if( tema > 64.8645 )
								ret := 0.000000
					if( ema2 > 65.8762 )
						if( tema <= 73.1438 )
							if( k <= 8.03623 )
								ret := -0.714286 // sell
							if( k > 8.03623 )
								ret := -1.000000 // sell
						if( tema > 73.1438 )
							if( d_k <= 28.8061 )
								ret := 0.400000
							if( d_k > 28.8061 )
								ret := -0.750000 // sell
		if( ema12 > -0.106011 )
			if( ema1 <= 53.984 )
				if( rsi1 <= 29.2218 )
					if( tema <= 51.7041 )
						ret := -0.500000
					if( tema > 51.7041 )
						if( ema1 <= 53.8608 )
							if( rsi1 <= 19.2941 )
								ret := 0.285714
							if( rsi1 > 19.2941 )
								if( d_k <= -4.63634 )
									ret := 0.333333
								if( d_k > -4.63634 )
									ret := 0.900000 // buy
						if( ema1 > 53.8608 )
							ret := 0.000000
				if( rsi1 > 29.2218 )
					if( d_k <= -11.8874 )
						if( ema2 <= 51.9352 )
							if( smoothK_k <= 62.749 )
								ret := -0.250000
							if( smoothK_k > 62.749 )
								if( k <= 82.4028 )
									ret := -0.750000 // sell
								if( k > 82.4028 )
									ret := -1.000000 // sell
						if( ema2 > 51.9352 )
							if( smoothK_k <= 78.5549 )
								if( k <= 44.4666 )
									ret := 0.350000
								if( k > 44.4666 )
									ret := -0.541667
							if( smoothK_k > 78.5549 )
								if( smoothK_k <= 86.3165 )
									ret := 0.782609 // buy
								if( smoothK_k > 86.3165 )
									ret := 0.086957
					if( d_k > -11.8874 )
						if( k <= 30.4475 )
							if( ema13 <= -0.191404 )
								ret := -1.000000 // sell
							if( ema13 > -0.191404 )
								if( ema2 <= 53.945 )
									ret := -0.041056
								if( ema2 > 53.945 )
									ret := 0.722222 // buy
						if( k > 30.4475 )
							if( rsi1 <= 59.4044 )
								if( smoothD_d <= 55.8053 )
									ret := 0.626374
								if( smoothD_d > 55.8053 )
									ret := 0.275964
							if( rsi1 > 59.4044 )
								if( ema2 <= 50.8463 )
									ret := -0.485714
								if( ema2 > 50.8463 )
									ret := 0.202073
			if( ema1 > 53.984 )
				if( ema12 <= 0.181971 )
					if( ema13 <= 0.36311 )
						if( d_k <= -1.55443 )
							if( tema <= 62.4268 )
								if( d <= 69.5284 )
									ret := 0.010115
								if( d > 69.5284 )
									ret := -0.116431
							if( tema > 62.4268 )
								if( smoothK_k <= 8.12038 )
									ret := -0.076728
								if( smoothK_k > 8.12038 )
									ret := 0.055056
						if( d_k > -1.55443 )
							if( d_k <= 28.5341 )
								if( rsi1 <= 51.6809 )
									ret := 0.083171
								if( rsi1 > 51.6809 )
									ret := 0.038397
							if( d_k > 28.5341 )
								if( smoothD_d <= 66.1528 )
									ret := -0.147436
								if( smoothD_d > 66.1528 )
									ret := -0.705882 // sell
					if( ema13 > 0.36311 )
						if( tema <= 66.1543 )
							if( rsi1 <= 75.283 )
								ret := 1.000000 // buy
							if( rsi1 > 75.283 )
								if( d <= 79.7085 )
									ret := 0.250000
								if( d > 79.7085 )
									ret := 1.000000 // buy
						if( tema > 66.1543 )
							if( rsi1 <= 53.4343 )
								ret := -0.750000 // sell
							if( rsi1 > 53.4343 )
								if( rsi1 <= 58.1039 )
									ret := 1.000000 // buy
								if( rsi1 > 58.1039 )
									ret := 0.275000
				if( ema12 > 0.181971 )
					if( d_k <= -13.2424 )
						if( d <= 55.4804 )
							if( smoothK_k <= 57.6688 )
								ret := -1.000000 // sell
							if( smoothK_k > 57.6688 )
								if( smoothK_k <= 67.9878 )
									ret := 0.333333
								if( smoothK_k > 67.9878 )
									ret := -0.750000 // sell
						if( d > 55.4804 )
							if( rsi1 <= 91.9674 )
								if( d_k <= -19.1686 )
									ret := 0.500000
								if( d_k > -19.1686 )
									ret := 0.851852 // buy
							if( rsi1 > 91.9674 )
								ret := -0.200000
					if( d_k > -13.2424 )
						if( ema1 <= 70.8724 )
							if( ema12 <= 0.994738 )
								if( k <= 1.02725 )
									ret := 0.666667
								if( k > 1.02725 )
									ret := -0.366242
							if( ema12 > 0.994738 )
								ret := 1.000000 // buy
						if( ema1 > 70.8724 )
							if( rsi1 <= 57.6694 )
								ret := 1.000000 // buy
							if( rsi1 > 57.6694 )
								if( k <= 83.6202 )
									ret := -0.219178
								if( k > 83.6202 )
									ret := 0.234234
	if( d > 94.8675 )
		if( ema12 <= 1.09611 )
			if( rsi1 <= 77.876 )
				if( ema12 <= 0.030905 )
					if( d <= 99.036 )
						if( rsi1 <= 57.0185 )
							if( smoothK_k <= 90.7616 )
								if( d_k <= 3.12459 )
									ret := 0.482759
								if( d_k > 3.12459 )
									ret := -0.093168
							if( smoothK_k > 90.7616 )
								if( k <= 99.9838 )
									ret := -0.278107
								if( k > 99.9838 )
									ret := 0.041667
						if( rsi1 > 57.0185 )
							if( ema13 <= -0.014804 )
								if( tema <= 61.3764 )
									ret := 0.638889
								if( tema > 61.3764 )
									ret := 0.048193
							if( ema13 > -0.014804 )
								if( ema2 <= 67.4493 )
									ret := -0.057751
								if( ema2 > 67.4493 )
									ret := 0.084746
					if( d > 99.036 )
						if( ema3 <= 52.3366 )
							ret := -1.000000 // sell
						if( ema3 > 52.3366 )
							if( ema2 <= 63.1078 )
								if( d_k <= 0.022422 )
									ret := 0.620000
								if( d_k > 0.022422 )
									ret := 0.270270
							if( ema2 > 63.1078 )
								if( ema2 <= 78.3031 )
									ret := 0.034934
								if( ema2 > 78.3031 )
									ret := 0.534884
				if( ema12 > 0.030905 )
					if( ema13 <= 0.016545 )
						if( d <= 96.2887 )
							ret := 0.142857
						if( d > 96.2887 )
							if( d <= 99.987 )
								if( ema12 <= 0.034369 )
									ret := -0.571429
								if( ema12 > 0.034369 )
									ret := -0.972222 // sell
							if( d > 99.987 )
								ret := -0.285714
					if( ema13 > 0.016545 )
						if( ema1 <= 77.4655 )
							if( ema2 <= 74.2504 )
								if( rsi1 <= 62.0973 )
									ret := -0.360360
								if( rsi1 > 62.0973 )
									ret := -0.097842
							if( ema2 > 74.2504 )
								if( k <= 92.9264 )
									ret := -0.161290
								if( k > 92.9264 )
									ret := -0.564220
						if( ema1 > 77.4655 )
							if( ema1 <= 81.0994 )
								if( d_k <= -0.251458 )
									ret := -0.243590
								if( d_k > -0.251458 )
									ret := 0.423358
							if( ema1 > 81.0994 )
								if( ema12 <= 0.108428 )
									ret := -0.233766
								if( ema12 > 0.108428 )
									ret := -0.812500 // sell
			if( rsi1 > 77.876 )
				if( rsi1 <= 90.5239 )
					if( rsi1 <= 86.5856 )
						if( ema12 <= 0.13189 )
							if( tema <= 61.6342 )
								if( ema1 <= 58.2963 )
									ret := 0.375000
								if( ema1 > 58.2963 )
									ret := -0.251969
							if( tema > 61.6342 )
								if( ema13 <= 0.113865 )
									ret := 0.059480
								if( ema13 > 0.113865 )
									ret := 0.256338
						if( ema12 > 0.13189 )
							if( rsi1 <= 80.4587 )
								if( ema1 <= 65.2222 )
									ret := -0.562500
								if( ema1 > 65.2222 )
									ret := 0.533333
							if( rsi1 > 80.4587 )
								if( ema2 <= 79.8017 )
									ret := -0.309524
								if( ema2 > 79.8017 )
									ret := -0.935484 // sell
					if( rsi1 > 86.5856 )
						if( tema <= 71.6552 )
							if( d_k <= -0.052913 )
								if( tema <= 55.5915 )
									ret := -1.000000 // sell
								if( tema > 55.5915 )
									ret := 0.520833
							if( d_k > -0.052913 )
								if( ema2 <= 63.8526 )
									ret := 0.388889
								if( ema2 > 63.8526 )
									ret := -0.181818
						if( tema > 71.6552 )
							if( ema3 <= 80.7581 )
								if( ema12 <= 0.132991 )
									ret := 0.350000
								if( ema12 > 0.132991 )
									ret := 0.898305 // buy
							if( ema3 > 80.7581 )
								if( ema12 <= 0.133665 )
									ret := 0.000000
								if( ema12 > 0.133665 )
									ret := -1.000000 // sell
				if( rsi1 > 90.5239 )
					if( smoothK_k <= 96.7974 )
						if( ema12 <= 0.194353 )
							if( rsi1 <= 92.9644 )
								if( ema12 <= 0.101629 )
									ret := -0.160000
								if( ema12 > 0.101629 )
									ret := -0.681818
							if( rsi1 > 92.9644 )
								if( d <= 99.5653 )
									ret := 0.000000
								if( d > 99.5653 )
									ret := 0.444444
						if( ema12 > 0.194353 )
							if( tema <= 64.8301 )
								ret := -0.428571
							if( tema > 64.8301 )
								if( d_k <= -2.61592 )
									ret := -0.500000
								if( d_k > -2.61592 )
									ret := 0.702703 // buy
					if( smoothK_k > 96.7974 )
						if( ema2 <= 74.0502 )
							if( ema12 <= 0.076525 )
								ret := 0.000000
							if( ema12 > 0.076525 )
								if( rsi1 <= 96.3324 )
									ret := -0.783333 // sell
								if( rsi1 > 96.3324 )
									ret := -0.333333
						if( ema2 > 74.0502 )
							if( rsi1 <= 98.4408 )
								ret := 0.000000
							if( rsi1 > 98.4408 )
								ret := -0.250000
		if( ema12 > 1.09611 )
			ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_SHOP_1Min_9fb20c01(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)

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


