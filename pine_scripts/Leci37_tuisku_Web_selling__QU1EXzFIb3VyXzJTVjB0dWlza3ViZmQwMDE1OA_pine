//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: AMD_1Hour_2SV0_bfd00158 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AMD_1Hour_2SV0_bfd00158", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AMD_1Hour_bfd00158(rsi1, smoothK_k, d_k, k, d, smoothD_d, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6,max_features=sqrt, min_samples_split=10,random_state=843828734)
	if( d_k <= -4.09208 )
		if( VIM <= 0.967924 )
			if( smoothD_d <= 87.3291 )
				if( k <= 99.6964 )
					if( d_k <= -9.39817 )
						if( smoothD_d <= 85.0398 )
							ret := 0.043527
						if( smoothD_d > 85.0398 )
							ret := -0.666667
					if( d_k > -9.39817 )
						if( smoothD_d <= 0.627021 )
							ret := 0.777778 // buy
						if( smoothD_d > 0.627021 )
							ret := -0.187078
				if( k > 99.6964 )
					if( smoothD_d <= 84.3188 )
						if( VIP_VIM <= 0.614444 )
							ret := 0.258824
						if( VIP_VIM > 0.614444 )
							ret := 0.800000 // buy
					if( smoothD_d > 84.3188 )
						if( VIP <= 1.1967 )
							ret := -0.588235
						if( VIP > 1.1967 )
							ret := 0.214286
			if( smoothD_d > 87.3291 )
				if( smoothK_k <= 96.2497 )
					if( VIM <= 0.68424 )
						if( smoothD_d <= 88.2459 )
							ret := 0.333333
						if( smoothD_d > 88.2459 )
							ret := 0.862069 // buy
					if( VIM > 0.68424 )
						if( VIP <= 1.30751 )
							ret := 0.490909
						if( VIP > 1.30751 )
							ret := -0.777778 // sell
				if( smoothK_k > 96.2497 )
					if( d <= 95.7105 )
						if( d <= 95.2186 )
							ret := 0.070588
						if( d > 95.2186 )
							ret := 0.451613
					if( d > 95.7105 )
						ret := -1.000000 // sell
		if( VIM > 0.967924 )
			if( VIP <= 1.0135 )
				if( VIP <= 0.945698 )
					if( d_k <= -30.0697 )
						if( VIP <= 0.873695 )
							ret := 0.000000
						if( VIP > 0.873695 )
							ret := 0.818182 // buy
					if( d_k > -30.0697 )
						if( d_k <= -23.459 )
							ret := -0.111969
						if( d_k > -23.459 )
							ret := 0.123273
				if( VIP > 0.945698 )
					if( d <= 93.7826 )
						if( smoothD_d <= 85.0358 )
							ret := 0.007541
						if( smoothD_d > 85.0358 )
							ret := -0.421875
					if( d > 93.7826 )
						if( k <= 99.9558 )
							ret := 0.888889 // buy
						if( k > 99.9558 )
							ret := 0.454545
			if( VIP > 1.0135 )
				if( smoothD_d <= 81.5777 )
					if( d_k <= -9.11561 )
						if( VIP_VIM <= 0.116651 )
							ret := 0.184915
						if( VIP_VIM > 0.116651 )
							ret := 0.422619
					if( d_k > -9.11561 )
						if( d_k <= -8.28918 )
							ret := -0.237500
						if( d_k > -8.28918 )
							ret := 0.037406
				if( smoothD_d > 81.5777 )
					if( k <= 99.9913 )
						if( smoothD_d <= 87.3249 )
							ret := 0.723810 // buy
						if( smoothD_d > 87.3249 )
							ret := 0.369565
					if( k > 99.9913 )
						if( VIP_VIM <= -0.020336 )
							ret := -0.750000 // sell
						if( VIP_VIM > -0.020336 )
							ret := 0.192308
	if( d_k > -4.09208 )
		if( smoothD_d <= 0.793605 )
			if( rsi1 <= 12.3254 )
				if( rsi1 <= 8.16631 )
					if( VIM <= 1.45509 )
						if( smoothK_k <= 1.26919 )
							ret := -0.446970
						if( smoothK_k > 1.26919 )
							ret := 0.833333 // buy
					if( VIM > 1.45509 )
						if( d <= 0.097762 )
							ret := 0.750000 // buy
						if( d > 0.097762 )
							ret := 0.024390
				if( rsi1 > 8.16631 )
					if( smoothD_d <= 0.199377 )
						if( VIM <= 1.35244 )
							ret := 0.730159 // buy
						if( VIM > 1.35244 )
							ret := 0.174194
					if( smoothD_d > 0.199377 )
						if( smoothK_k <= 2.64316 )
							ret := -0.916667 // sell
						if( smoothK_k > 2.64316 )
							ret := 0.333333
			if( rsi1 > 12.3254 )
				if( VIP <= 0.865652 )
					if( smoothK_k <= 2.72767 )
						if( d_k <= 3.14736 )
							ret := -0.366496
						if( d_k > 3.14736 )
							ret := 0.444444
					if( smoothK_k > 2.72767 )
						if( d <= 3.73559 )
							ret := 0.262295
						if( d > 3.73559 )
							ret := -0.750000 // sell
				if( VIP > 0.865652 )
					if( rsi1 <= 57.3358 )
						if( VIP_VIM <= 0.110002 )
							ret := -0.013255
						if( VIP_VIM > 0.110002 )
							ret := 0.565789
					if( rsi1 > 57.3358 )
						if( VIP <= 1.28722 )
							ret := -0.500000
						if( VIP > 1.28722 )
							ret := 0.800000 // buy
		if( smoothD_d > 0.793605 )
			if( VIM <= 1.29064 )
				if( VIP_VIM <= 0.11157 )
					if( d <= 99.2755 )
						if( d_k <= -2.84373 )
							ret := -0.227034
						if( d_k > -2.84373 )
							ret := -0.044288
					if( d > 99.2755 )
						if( rsi1 <= 62.6015 )
							ret := 0.361905
						if( rsi1 > 62.6015 )
							ret := -1.000000 // sell
				if( VIP_VIM > 0.11157 )
					if( rsi1 <= 79.5803 )
						if( k <= 90.8754 )
							ret := 0.012694
						if( k > 90.8754 )
							ret := 0.151857
					if( rsi1 > 79.5803 )
						if( smoothD_d <= 93.085 )
							ret := -0.200807
						if( smoothD_d > 93.085 )
							ret := 0.046843
			if( VIM > 1.29064 )
				if( smoothD_d <= 7.65218 )
					if( smoothK_k <= 0.837336 )
						if( VIP_VIM <= -0.400205 )
							ret := 0.007194
						if( VIP_VIM > -0.400205 )
							ret := 0.615385
					if( smoothK_k > 0.837336 )
						if( rsi1 <= 21.2277 )
							ret := 0.625000
						if( rsi1 > 21.2277 )
							ret := 0.064935
				if( smoothD_d > 7.65218 )
					if( smoothD_d <= 17.9899 )
						if( k <= 17.918 )
							ret := 0.105263
						if( k > 17.918 )
							ret := -0.733333 // sell
					if( smoothD_d > 17.9899 )
						if( d <= 28.5458 )
							ret := 0.514286
						if( d > 28.5458 )
							ret := 0.022556
	
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
float op_operation = decision_tree_0_AMD_1Hour_bfd00158(rsi1, smoothK_k, d_k, k, d, smoothD_d, VIP, VIM, VIP_VIM)

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


