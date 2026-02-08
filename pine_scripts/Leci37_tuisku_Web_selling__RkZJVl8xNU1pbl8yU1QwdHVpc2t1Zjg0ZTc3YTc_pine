//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: FFIV_15Min_2ST0_f84e77a7 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_FFIV_15Min_2ST0_f84e77a7", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_FFIV_15Min_f84e77a7(d, d_k, smoothK_k, k, rsi1, smoothD_d, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( d <= 12.7775 )
		if( ema12 <= 1.30444 )
			if( k <= 4.82758 )
				if( ema1 <= 111.969 )
					if( ema13 <= -3.21683 )
						ret := 0.250000
					if( ema13 > -3.21683 )
						if( k <= 3.65688 )
							ret := 1.000000 // buy
						if( k > 3.65688 )
							ret := 0.909091 // buy
				if( ema1 > 111.969 )
					if( ema3 <= 170.648 )
						if( ema2 <= 167.833 )
							if( ema13 <= -0.998828 )
								if( ema1 <= 163.62 )
									ret := -0.096552
								if( ema1 > 163.62 )
									ret := -0.805970 // sell
							if( ema13 > -0.998828 )
								if( ema2 <= 167.515 )
									ret := 0.003861
								if( ema2 > 167.515 )
									ret := 0.764706 // buy
						if( ema2 > 167.833 )
							if( d <= 9.09123 )
								if( tema <= 165.544 )
									ret := -1.000000 // sell
								if( tema > 165.544 )
									ret := -0.517413
							if( d > 9.09123 )
								ret := 0.750000 // buy
					if( ema3 > 170.648 )
						if( ema1 <= 174.686 )
							if( rsi1 <= 43.6891 )
								if( d_k <= -0.084928 )
									ret := 0.313131
								if( d_k > -0.084928 )
									ret := 0.626087
							if( rsi1 > 43.6891 )
								if( rsi1 <= 51.6145 )
									ret := -0.071429
								if( rsi1 > 51.6145 )
									ret := -0.727273 // sell
						if( ema1 > 174.686 )
							if( rsi1 <= 27.8133 )
								if( tema <= 204.497 )
									ret := 0.227207
								if( tema > 204.497 )
									ret := -0.195652
							if( rsi1 > 27.8133 )
								if( ema2 <= 192.022 )
									ret := 0.044397
								if( ema2 > 192.022 )
									ret := -0.191946
			if( k > 4.82758 )
				if( d_k <= -7.25262 )
					if( ema1 <= 208.438 )
						if( ema1 <= 144.587 )
							if( k <= 23.26 )
								if( k <= 13.2256 )
									ret := -0.409091
								if( k > 13.2256 )
									ret := 0.366848
							if( k > 23.26 )
								if( ema13 <= -0.192272 )
									ret := -0.285714
								if( ema13 > -0.192272 )
									ret := -0.677419
						if( ema1 > 144.587 )
							if( ema3 <= 171.646 )
								if( d_k <= -13.6024 )
									ret := -0.892857 // sell
								if( d_k > -13.6024 )
									ret := -0.209040
							if( ema3 > 171.646 )
								if( rsi1 <= 55.269 )
									ret := 0.214953
								if( rsi1 > 55.269 )
									ret := -0.506494
					if( ema1 > 208.438 )
						if( d_k <= -12.4793 )
							ret := 1.000000 // buy
						if( d_k > -12.4793 )
							if( ema1 <= 224.293 )
								if( d <= 10.4133 )
									ret := -0.111111
								if( d > 10.4133 )
									ret := 0.500000
							if( ema1 > 224.293 )
								if( k <= 18.8402 )
									ret := 0.944444 // buy
								if( k > 18.8402 )
									ret := 0.428571
				if( d_k > -7.25262 )
					if( ema3 <= 99.361 )
						if( ema3 <= 97.9757 )
							ret := 1.000000 // buy
						if( ema3 > 97.9757 )
							ret := 0.888889 // buy
					if( ema3 > 99.361 )
						if( rsi1 <= 68.5723 )
							if( ema2 <= 130.885 )
								if( ema1 <= 128.2 )
									ret := -0.188940
								if( ema1 > 128.2 )
									ret := -0.626582
							if( ema2 > 130.885 )
								if( ema13 <= -2.25101 )
									ret := -0.282051
								if( ema13 > -2.25101 )
									ret := -0.073307
						if( rsi1 > 68.5723 )
							if( tema <= 149.866 )
								ret := -0.800000 // sell
							if( tema > 149.866 )
								if( ema12 <= 0.447927 )
									ret := 0.625000
								if( ema12 > 0.447927 )
									ret := 0.962963 // buy
		if( ema12 > 1.30444 )
			ret := -1.000000 // sell
	if( d > 12.7775 )
		if( ema1 <= 144.184 )
			if( ema1 <= 90.7597 )
				if( ema3 <= 91.6441 )
					if( smoothD_d <= 74.0051 )
						ret := 0.923077 // buy
					if( smoothD_d > 74.0051 )
						ret := 1.000000 // buy
				if( ema3 > 91.6441 )
					ret := 0.400000
			if( ema1 > 90.7597 )
				if( ema3 <= 90.8964 )
					ret := 1.000000 // buy
				if( ema3 > 90.8964 )
					if( k <= 99.9726 )
						if( ema2 <= 90.9712 )
							if( d_k <= -2.52246 )
								ret := -0.909091 // sell
							if( d_k > -2.52246 )
								ret := -1.000000 // sell
						if( ema2 > 90.9712 )
							if( smoothK_k <= -2.66016 )
								if( ema2 <= 140.241 )
									ret := 0.639640
								if( ema2 > 140.241 )
									ret := 0.026316
							if( smoothK_k > -2.66016 )
								if( rsi1 <= 75.4072 )
									ret := 0.062017
								if( rsi1 > 75.4072 )
									ret := 0.203633
					if( k > 99.9726 )
						if( ema12 <= 0.55938 )
							if( rsi1 <= 56.7878 )
								if( ema1 <= 138.302 )
									ret := -0.455556
								if( ema1 > 138.302 )
									ret := 0.000000
							if( rsi1 > 56.7878 )
								if( ema12 <= -0.027026 )
									ret := -0.437500
								if( ema12 > -0.027026 )
									ret := 0.095930
						if( ema12 > 0.55938 )
							if( d <= 99.9963 )
								if( ema3 <= 132.399 )
									ret := -0.813953 // sell
								if( ema3 > 132.399 )
									ret := -0.530120
							if( d > 99.9963 )
								if( ema1 <= 142.904 )
									ret := 0.200000
								if( ema1 > 142.904 )
									ret := -0.642857
		if( ema1 > 144.184 )
			if( ema2 <= 154.547 )
				if( ema13 <= 1.93116 )
					if( d <= 46.2884 )
						if( tema <= 151.955 )
							if( tema <= 143.706 )
								if( smoothD_d <= 27.3047 )
									ret := -1.000000 // sell
								if( smoothD_d > 27.3047 )
									ret := -0.076923
							if( tema > 143.706 )
								if( smoothD_d <= 11.1963 )
									ret := 0.243421
								if( smoothD_d > 11.1963 )
									ret := -0.147413
						if( tema > 151.955 )
							if( smoothK_k <= 53.9206 )
								if( ema3 <= 154.833 )
									ret := -0.575980
								if( ema3 > 154.833 )
									ret := 0.214286
							if( smoothK_k > 53.9206 )
								if( ema12 <= -0.067069 )
									ret := -0.307692
								if( ema12 > -0.067069 )
									ret := 0.560000
					if( d > 46.2884 )
						if( ema13 <= 0.308325 )
							if( ema3 <= 154.357 )
								if( k <= 71.8083 )
									ret := -0.037764
								if( k > 71.8083 )
									ret := 0.092564
							if( ema3 > 154.357 )
								if( k <= 89.1383 )
									ret := -0.500000
								if( k > 89.1383 )
									ret := -1.000000 // sell
						if( ema13 > 0.308325 )
							if( ema2 <= 148.99 )
								if( ema2 <= 146.942 )
									ret := -0.072600
								if( ema2 > 146.942 )
									ret := -0.344203
							if( ema2 > 148.99 )
								if( d_k <= 9.48977 )
									ret := 0.150623
								if( d_k > 9.48977 )
									ret := -0.322581
				if( ema13 > 1.93116 )
					if( rsi1 <= 77.9046 )
						if( d_k <= 18.5799 )
							if( k <= 47.7587 )
								ret := 0.045455
							if( k > 47.7587 )
								if( ema1 <= 152.044 )
									ret := -0.541667
								if( ema1 > 152.044 )
									ret := -1.000000 // sell
						if( d_k > 18.5799 )
							ret := 0.941176 // buy
					if( rsi1 > 77.9046 )
						if( smoothD_d <= 65.6693 )
							if( d_k <= -9.73145 )
								ret := -0.764706 // sell
							if( d_k > -9.73145 )
								ret := 0.588235
						if( smoothD_d > 65.6693 )
							if( ema12 <= 1.254 )
								if( d <= 90.5754 )
									ret := 0.833333 // buy
								if( d > 90.5754 )
									ret := -0.294118
							if( ema12 > 1.254 )
								if( ema2 <= 153.849 )
									ret := 0.916667 // buy
								if( ema2 > 153.849 )
									ret := 0.300000
			if( ema2 > 154.547 )
				if( smoothK_k <= 18.956 )
					if( ema2 <= 185.335 )
						if( ema12 <= 0.48664 )
							if( d <= 34.0825 )
								if( ema12 <= -0.655331 )
									ret := -0.170833
								if( ema12 > -0.655331 )
									ret := 0.104155
							if( d > 34.0825 )
								if( ema3 <= 162.254 )
									ret := 0.148515
								if( ema3 > 162.254 )
									ret := -0.360976
						if( ema12 > 0.48664 )
							if( ema13 <= 1.62993 )
								if( ema1 <= 168.305 )
									ret := -0.600000
								if( ema1 > 168.305 )
									ret := -0.916667 // sell
							if( ema13 > 1.62993 )
								if( rsi1 <= 71.0876 )
									ret := 0.000000
								if( rsi1 > 71.0876 )
									ret := -0.733333 // sell
					if( ema2 > 185.335 )
						if( ema1 <= 185.674 )
							if( d <= 24.5686 )
								if( ema2 <= 185.813 )
									ret := 1.000000 // buy
								if( ema2 > 185.813 )
									ret := 0.733333 // buy
							if( d > 24.5686 )
								ret := 0.454545
						if( ema1 > 185.674 )
							if( smoothK_k <= 2.81034 )
								if( ema1 <= 202.578 )
									ret := -0.293706
								if( ema1 > 202.578 )
									ret := 0.079268
							if( smoothK_k > 2.81034 )
								if( k <= 11.9831 )
									ret := 0.439673
								if( k > 11.9831 )
									ret := 0.110914
				if( smoothK_k > 18.956 )
					if( tema <= 201.47 )
						if( d_k <= -29.7304 )
							if( ema2 <= 159.169 )
								ret := -0.375000
							if( ema2 > 159.169 )
								if( ema12 <= 0.605137 )
									ret := 0.607143
								if( ema12 > 0.605137 )
									ret := -0.500000
						if( d_k > -29.7304 )
							if( ema1 <= 200.926 )
								if( ema3 <= 199.889 )
									ret := -0.002642
								if( ema3 > 199.889 )
									ret := -0.301471
							if( ema1 > 200.926 )
								if( smoothK_k <= 85.0673 )
									ret := 0.422111
								if( smoothK_k > 85.0673 )
									ret := -0.714286 // sell
					if( tema > 201.47 )
						if( d <= 41.6045 )
							if( ema13 <= 1.95642 )
								if( tema <= 218.004 )
									ret := -0.260776
								if( tema > 218.004 )
									ret := -0.076923
							if( ema13 > 1.95642 )
								if( smoothD_d <= 34.4898 )
									ret := -1.000000 // sell
								if( smoothD_d > 34.4898 )
									ret := -0.888889 // sell
						if( d > 41.6045 )
							if( d <= 75.555 )
								if( ema1 <= 239.116 )
									ret := 0.066819
								if( ema1 > 239.116 )
									ret := -0.490000
							if( d > 75.555 )
								if( ema13 <= 3.92452 )
									ret := -0.141080
								if( ema13 > 3.92452 )
									ret := -0.666667
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_FFIV_15Min_f84e77a7(d, d_k, smoothK_k, k, rsi1, smoothD_d, ema12, ema3, ema13, tema, ema1, ema2)

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


