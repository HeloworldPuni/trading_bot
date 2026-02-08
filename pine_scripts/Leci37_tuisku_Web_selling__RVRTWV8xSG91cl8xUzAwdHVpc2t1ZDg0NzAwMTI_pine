//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI
// ID_model: ETSY_1Hour_1S00_d8470012 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ETSY_1Hour_1S00_d8470012", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ETSY_1Hour_d8470012(d, d_k, smoothK_k, k, rsi1, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( smoothK_k <= 0.411083 )
		if( rsi1 <= 13.6085 )
			if( smoothK_k <= -0.752895 )
				if( d <= 0.130068 )
					if( d_k <= -0.015108 )
						if( smoothD_d <= -2.948 )
							ret := -0.833333 // sell
						if( smoothD_d > -2.948 )
							ret := -1.000000 // sell
					if( d_k > -0.015108 )
						if( d <= 0.005019 )
							ret := -0.266667
						if( d > 0.005019 )
							ret := 0.250000
				if( d > 0.130068 )
					if( d_k <= 0.982076 )
						if( rsi1 <= 6.84111 )
							ret := -0.250000
						if( rsi1 > 6.84111 )
							ret := 0.465753
					if( d_k > 0.982076 )
						if( smoothD_d <= 2.77708 )
							ret := -0.349206
						if( smoothD_d > 2.77708 )
							ret := 0.300000
			if( smoothK_k > -0.752895 )
				if( rsi1 <= 10.1216 )
					if( d <= 2.6514 )
						ret := -0.900000 // sell
					if( d > 2.6514 )
						ret := -1.000000 // sell
				if( rsi1 > 10.1216 )
					ret := -0.666667
		if( rsi1 > 13.6085 )
			if( d_k <= 0.087436 )
				if( smoothD_d <= -1.57192 )
					if( rsi1 <= 47.773 )
						if( d <= 0.668988 )
							ret := 0.278607
						if( d > 0.668988 )
							ret := -0.117241
					if( rsi1 > 47.773 )
						if( smoothD_d <= -1.98878 )
							ret := 0.722222 // buy
						if( smoothD_d > -1.98878 )
							ret := 0.352941
				if( smoothD_d > -1.57192 )
					if( d_k <= -0.967606 )
						if( smoothK_k <= 0.070748 )
							ret := 1.000000 // buy
						if( smoothK_k > 0.070748 )
							ret := 0.625000
					if( d_k > -0.967606 )
						if( rsi1 <= 25.032 )
							ret := 0.733333 // buy
						if( rsi1 > 25.032 )
							ret := 0.299145
			if( d_k > 0.087436 )
				if( d <= 4.98667 )
					if( rsi1 <= 24.5073 )
						if( smoothK_k <= -0.456556 )
							ret := -0.206704
						if( smoothK_k > -0.456556 )
							ret := -0.947368 // sell
					if( rsi1 > 24.5073 )
						if( d_k <= 1.73854 )
							ret := 0.293333
						if( d_k > 1.73854 )
							ret := -0.100917
				if( d > 4.98667 )
					if( k <= 2.94358 )
						if( rsi1 <= 21.2939 )
							ret := 0.509804
						if( rsi1 > 21.2939 )
							ret := 0.078859
					if( k > 2.94358 )
						if( rsi1 <= 37.1921 )
							ret := 0.289474
						if( rsi1 > 37.1921 )
							ret := 0.716667 // buy
	if( smoothK_k > 0.411083 )
		if( smoothD_d <= 2.80076 )
			if( smoothK_k <= 8.53798 )
				if( k <= 9.81795 )
					if( rsi1 <= 31.1751 )
						if( rsi1 <= 26.353 )
							ret := -0.179221
						if( rsi1 > 26.353 )
							ret := 0.242188
					if( rsi1 > 31.1751 )
						if( smoothD_d <= 0.427605 )
							ret := -0.125000
						if( smoothD_d > 0.427605 )
							ret := -0.388268
				if( k > 9.81795 )
					if( d_k <= -5.95393 )
						ret := -0.333333
					if( d_k > -5.95393 )
						if( rsi1 <= 49.8014 )
							ret := 0.630435
						if( rsi1 > 49.8014 )
							ret := -0.187500
			if( smoothK_k > 8.53798 )
				if( smoothD_d <= 1.82255 )
					ret := -0.250000
				if( smoothD_d > 1.82255 )
					if( d <= 5.44363 )
						if( d_k <= -7.72848 )
							ret := -1.000000 // sell
						if( d_k > -7.72848 )
							ret := -0.533333
					if( d > 5.44363 )
						if( d <= 5.71828 )
							ret := -1.000000 // sell
						if( d > 5.71828 )
							ret := -0.818182 // sell
		if( smoothD_d > 2.80076 )
			if( rsi1 <= 24.7603 )
				if( d <= 37.2181 )
					if( k <= 15.9959 )
						if( smoothD_d <= 6.31609 )
							ret := -0.238342
						if( smoothD_d > 6.31609 )
							ret := 0.055814
					if( k > 15.9959 )
						if( d_k <= -14.3842 )
							ret := 0.434783
						if( d_k > -14.3842 )
							ret := -0.536986
				if( d > 37.2181 )
					if( smoothK_k <= 83.159 )
						if( d_k <= -10.6177 )
							ret := -0.578947
						if( d_k > -10.6177 )
							ret := 0.250000
					if( smoothK_k > 83.159 )
						if( k <= 90.8466 )
							ret := -0.428571
						if( k > 90.8466 )
							ret := -0.933333 // sell
			if( rsi1 > 24.7603 )
				if( smoothD_d <= 4.58055 )
					if( rsi1 <= 35.3621 )
						if( rsi1 <= 31.7428 )
							ret := 0.171429
						if( rsi1 > 31.7428 )
							ret := -0.452830
					if( rsi1 > 35.3621 )
						if( d_k <= -7.98773 )
							ret := -0.294118
						if( d_k > -7.98773 )
							ret := 0.482866
				if( smoothD_d > 4.58055 )
					if( d <= 14.8904 )
						if( d <= 12.7752 )
							ret := -0.036873
						if( d > 12.7752 )
							ret := -0.309886
					if( d > 14.8904 )
						if( d_k <= -15.6079 )
							ret := -0.115841
						if( d_k > -15.6079 )
							ret := 0.014887
	
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
float op_operation = decision_tree_0_ETSY_1Hour_d8470012(d, d_k, smoothK_k, k, rsi1, smoothD_d)

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


