//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: AFRM_1Min_1T00_b9de3e65 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AFRM_1Min_1T00_b9de3e65", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AFRM_1Min_b9de3e65(ema3, tema, ema2, ema12, ema13, ema1)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ema12 <= 0.000451 )
		if( ema1 <= 32.0376 )
			if( ema13 <= -0.280196 )
				if( ema2 <= 24.0363 )
					if( tema <= 22.8224 )
						if( tema <= 22.6682 )
							ret := -0.250000
						if( tema > 22.6682 )
							if( ema3 <= 23.5172 )
								ret := 1.000000 // buy
							if( ema3 > 23.5172 )
								ret := 0.500000
					if( tema > 22.8224 )
						if( tema <= 22.9154 )
							ret := -0.500000
						if( tema > 22.9154 )
							if( ema2 <= 23.9072 )
								ret := -1.000000 // sell
							if( ema2 > 23.9072 )
								ret := -0.750000 // sell
				if( ema2 > 24.0363 )
					if( ema1 <= 25.2482 )
						if( ema3 <= 25.0275 )
							if( ema1 <= 24.2036 )
								if( ema2 <= 24.3138 )
									ret := 1.000000 // buy
								if( ema2 > 24.3138 )
									ret := 0.333333
							if( ema1 > 24.2036 )
								ret := -0.500000
						if( ema3 > 25.0275 )
							if( ema12 <= -0.241756 )
								ret := 1.000000 // buy
							if( ema12 > -0.241756 )
								if( ema13 <= -0.413793 )
									ret := 0.500000
								if( ema13 > -0.413793 )
									ret := 0.941176 // buy
					if( ema1 > 25.2482 )
						if( ema12 <= -0.30425 )
							if( ema2 <= 31.5911 )
								if( ema13 <= -0.958143 )
									ret := 0.000000
								if( ema13 > -0.958143 )
									ret := -0.947368 // sell
							if( ema2 > 31.5911 )
								if( ema1 <= 31.6502 )
									ret := 0.750000 // buy
								if( ema1 > 31.6502 )
									ret := 0.500000
						if( ema12 > -0.30425 )
							if( tema <= 25.4496 )
								if( ema2 <= 25.6829 )
									ret := -0.500000
								if( ema2 > 25.6829 )
									ret := -1.000000 // sell
							if( tema > 25.4496 )
								if( tema <= 30.4019 )
									ret := 0.358974
								if( tema > 30.4019 )
									ret := 0.708029 // buy
			if( ema13 > -0.280196 )
				if( tema <= 24.3891 )
					if( ema1 <= 23.8755 )
						if( ema13 <= -0.114968 )
							if( tema <= 22.1079 )
								if( ema12 <= -0.090151 )
									ret := 1.000000 // buy
								if( ema12 > -0.090151 )
									ret := -0.083333
							if( tema > 22.1079 )
								if( ema12 <= -0.088121 )
									ret := -0.133333
								if( ema12 > -0.088121 )
									ret := -0.785714 // sell
						if( ema13 > -0.114968 )
							if( ema2 <= 22.567 )
								if( ema1 <= 21.9803 )
									ret := 0.714286 // buy
								if( ema1 > 21.9803 )
									ret := 1.000000 // buy
							if( ema2 > 22.567 )
								if( tema <= 22.7544 )
									ret := -1.000000 // sell
								if( tema > 22.7544 )
									ret := 0.222222
					if( ema1 > 23.8755 )
						if( ema1 <= 24.0981 )
							if( ema13 <= -0.211976 )
								ret := -0.200000
							if( ema13 > -0.211976 )
								if( ema3 <= 24.1496 )
									ret := 0.763636 // buy
								if( ema3 > 24.1496 )
									ret := 0.967213 // buy
						if( ema1 > 24.0981 )
							if( ema2 <= 24.3438 )
								if( ema1 <= 24.1966 )
									ret := 0.523810
								if( ema1 > 24.1966 )
									ret := -0.254902
							if( ema2 > 24.3438 )
								if( ema3 <= 24.4232 )
									ret := 0.759259 // buy
								if( ema3 > 24.4232 )
									ret := 0.325000
				if( tema > 24.3891 )
					if( tema <= 31.8981 )
						if( ema3 <= 24.8512 )
							if( ema13 <= -0.035785 )
								if( ema12 <= -0.037568 )
									ret := -0.134454
								if( ema12 > -0.037568 )
									ret := -0.561404
							if( ema13 > -0.035785 )
								if( ema2 <= 24.5578 )
									ret := -0.104478
								if( ema2 > 24.5578 )
									ret := 0.350877
						if( ema3 > 24.8512 )
							if( ema1 <= 24.979 )
								if( ema3 <= 24.9482 )
									ret := 0.121795
								if( ema3 > 24.9482 )
									ret := 0.600000
							if( ema1 > 24.979 )
								if( tema <= 24.9863 )
									ret := -0.770833 // sell
								if( tema > 24.9863 )
									ret := 0.091027
					if( tema > 31.8981 )
						if( ema3 <= 31.9509 )
							if( ema1 <= 31.953 )
								if( ema3 <= 31.9112 )
									ret := 0.000000
								if( ema3 > 31.9112 )
									ret := 0.772277 // buy
							if( ema1 > 31.953 )
								ret := 0.000000
						if( ema3 > 31.9509 )
							if( ema1 <= 31.9799 )
								if( ema1 <= 31.9636 )
									ret := 0.171053
								if( ema1 > 31.9636 )
									ret := -0.343750
							if( ema1 > 31.9799 )
								if( ema13 <= -0.103224 )
									ret := 0.602410
								if( ema13 > -0.103224 )
									ret := 0.245283
		if( ema1 > 32.0376 )
			if( ema2 <= 32.6757 )
				if( ema3 <= 32.3011 )
					if( tema <= 31.9451 )
						if( ema3 <= 32.191 )
							ret := -0.250000
						if( ema3 > 32.191 )
							if( ema2 <= 32.178 )
								if( ema2 <= 32.1411 )
									ret := 0.750000 // buy
								if( ema2 > 32.1411 )
									ret := 1.000000 // buy
							if( ema2 > 32.178 )
								ret := 0.500000
					if( tema > 31.9451 )
						if( ema2 <= 32.2667 )
							if( tema <= 32.1953 )
								if( ema3 <= 32.2307 )
									ret := -0.232779
								if( ema3 > 32.2307 )
									ret := -0.553846
							if( tema > 32.1953 )
								if( ema2 <= 32.258 )
									ret := 0.236842
								if( ema2 > 32.258 )
									ret := -0.454545
						if( ema2 > 32.2667 )
							if( ema12 <= -0.000193 )
								if( ema13 <= 0.002078 )
									ret := -0.775510 // sell
								if( ema13 > 0.002078 )
									ret := 0.000000
							if( ema12 > -0.000193 )
								ret := -0.250000
				if( ema3 > 32.3011 )
					if( tema <= 32.589 )
						if( tema <= 32.035 )
							if( ema1 <= 32.0768 )
								ret := 0.142857
							if( ema1 > 32.0768 )
								if( ema13 <= -0.249505 )
									ret := -0.642857
								if( ema13 > -0.249505 )
									ret := -1.000000 // sell
						if( tema > 32.035 )
							if( ema1 <= 32.249 )
								if( ema2 <= 32.2737 )
									ret := 0.000000
								if( ema2 > 32.2737 )
									ret := 0.609756
							if( ema1 > 32.249 )
								if( ema2 <= 32.3095 )
									ret := -0.409836
								if( ema2 > 32.3095 )
									ret := -0.027997
					if( tema > 32.589 )
						if( ema1 <= 32.6641 )
							if( tema <= 32.6201 )
								if( ema3 <= 32.67 )
									ret := -0.628571
								if( ema3 > 32.67 )
									ret := 0.400000
							if( tema > 32.6201 )
								if( tema <= 32.6375 )
									ret := -1.000000 // sell
								if( tema > 32.6375 )
									ret := -0.727273 // sell
						if( ema1 > 32.6641 )
							ret := 0.000000
			if( ema2 > 32.6757 )
				if( ema13 <= -0.877057 )
					if( tema <= 32.8789 )
						ret := -0.750000 // sell
					if( tema > 32.8789 )
						ret := -1.000000 // sell
				if( ema13 > -0.877057 )
					if( tema <= 37.1347 )
						if( tema <= 33.2202 )
							if( ema1 <= 33.3413 )
								if( ema1 <= 33.2448 )
									ret := 0.125000
								if( ema1 > 33.2448 )
									ret := -0.409836
							if( ema1 > 33.3413 )
								if( tema <= 33.1972 )
									ret := 0.947368 // buy
								if( tema > 33.1972 )
									ret := 0.181818
						if( tema > 33.2202 )
							if( ema12 <= -0.135215 )
								if( ema3 <= 34.8923 )
									ret := -0.776471 // sell
								if( ema3 > 34.8923 )
									ret := -0.390110
							if( ema12 > -0.135215 )
								if( ema2 <= 34.2447 )
									ret := -0.153914
								if( ema2 > 34.2447 )
									ret := 0.043020
					if( tema > 37.1347 )
						if( ema12 <= -0.192265 )
							if( ema3 <= 39.2148 )
								if( ema12 <= -0.21053 )
									ret := -0.542857
								if( ema12 > -0.21053 )
									ret := 0.333333
							if( ema3 > 39.2148 )
								if( tema <= 44.8925 )
									ret := 0.629344
								if( tema > 44.8925 )
									ret := -0.057692
						if( ema12 > -0.192265 )
							if( ema1 <= 38.1089 )
								if( ema2 <= 38.136 )
									ret := 0.284424
								if( ema2 > 38.136 )
									ret := 0.721311 // buy
							if( ema1 > 38.1089 )
								if( tema <= 45.4928 )
									ret := 0.070342
								if( tema > 45.4928 )
									ret := -0.090529
	if( ema12 > 0.000451 )
		if( ema3 <= 22.2444 )
			if( ema2 <= 22.0704 )
				if( ema12 <= 0.028195 )
					ret := 1.000000 // buy
				if( ema12 > 0.028195 )
					ret := -0.166667
			if( ema2 > 22.0704 )
				if( ema2 <= 22.1147 )
					if( ema2 <= 22.0927 )
						ret := 1.000000 // buy
					if( ema2 > 22.0927 )
						ret := 0.500000
				if( ema2 > 22.1147 )
					ret := 1.000000 // buy
		if( ema3 > 22.2444 )
			if( ema2 <= 45.6224 )
				if( tema <= 44.761 )
					if( tema <= 22.9605 )
						if( ema1 <= 22.57 )
							if( ema1 <= 22.5285 )
								ret := -0.400000
							if( ema1 > 22.5285 )
								ret := 0.600000
						if( ema1 > 22.57 )
							if( ema2 <= 22.8025 )
								if( ema1 <= 22.6291 )
									ret := -1.000000 // sell
								if( ema1 > 22.6291 )
									ret := 0.500000
							if( ema2 > 22.8025 )
								ret := -1.000000 // sell
					if( tema > 22.9605 )
						if( tema <= 23.6974 )
							ret := 1.000000 // buy
						if( tema > 23.6974 )
							if( ema3 <= 44.3349 )
								if( tema <= 44.389 )
									ret := 0.017549
								if( tema > 44.389 )
									ret := -0.333333
							if( ema3 > 44.3349 )
								if( ema13 <= 0.116887 )
									ret := 0.363128
								if( ema13 > 0.116887 )
									ret := -0.327869
				if( tema > 44.761 )
					if( ema3 <= 44.4216 )
						if( ema3 <= 44.3262 )
							ret := 0.000000
						if( ema3 > 44.3262 )
							ret := -1.000000 // sell
					if( ema3 > 44.4216 )
						if( ema12 <= 0.306187 )
							if( ema12 <= 0.227073 )
								if( tema <= 44.8968 )
									ret := -0.254464
								if( tema > 44.8968 )
									ret := -0.070064
							if( ema12 > 0.227073 )
								if( ema1 <= 45.4391 )
									ret := -1.000000 // sell
								if( ema1 > 45.4391 )
									ret := -0.750000 // sell
						if( ema12 > 0.306187 )
							if( ema13 <= 0.552453 )
								ret := 1.000000 // buy
							if( ema13 > 0.552453 )
								ret := 0.500000
			if( ema2 > 45.6224 )
				if( ema2 <= 46.6043 )
					if( ema2 <= 46.3185 )
						if( tema <= 46.3731 )
							if( ema13 <= 0.157775 )
								if( ema3 <= 45.6405 )
									ret := 0.473684
								if( ema3 > 45.6405 )
									ret := -0.166667
							if( ema13 > 0.157775 )
								if( tema <= 46.1813 )
									ret := 0.867925 // buy
								if( tema > 46.1813 )
									ret := 0.000000
						if( tema > 46.3731 )
							if( ema3 <= 46.1481 )
								if( tema <= 46.5126 )
									ret := -0.714286 // sell
								if( tema > 46.5126 )
									ret := -1.000000 // sell
							if( ema3 > 46.1481 )
								ret := -0.166667
					if( ema2 > 46.3185 )
						if( ema13 <= 0.262148 )
							if( ema3 <= 46.3098 )
								ret := 1.000000 // buy
							if( ema3 > 46.3098 )
								if( ema3 <= 46.3998 )
									ret := 0.725000 // buy
								if( ema3 > 46.3998 )
									ret := 0.907692 // buy
						if( ema13 > 0.262148 )
							ret := 0.000000
				if( ema2 > 46.6043 )
					if( ema1 <= 47.0989 )
						if( ema13 <= 0.176265 )
							if( ema13 <= 0.045994 )
								if( ema12 <= 0.03193 )
									ret := 0.000000
								if( ema12 > 0.03193 )
									ret := 0.800000 // buy
							if( ema13 > 0.045994 )
								if( tema <= 47.1121 )
									ret := -0.906977 // sell
								if( tema > 47.1121 )
									ret := -0.333333
						if( ema13 > 0.176265 )
							if( ema2 <= 46.9117 )
								if( ema13 <= 0.277752 )
									ret := 0.827586 // buy
								if( ema13 > 0.277752 )
									ret := -0.142857
							if( ema2 > 46.9117 )
								if( ema12 <= 0.104191 )
									ret := -1.000000 // sell
								if( ema12 > 0.104191 )
									ret := -0.750000 // sell
					if( ema1 > 47.0989 )
						if( ema1 <= 47.3502 )
							if( ema1 <= 47.2019 )
								if( ema12 <= 0.092381 )
									ret := 0.305556
								if( ema12 > 0.092381 )
									ret := -0.500000
							if( ema1 > 47.2019 )
								if( tema <= 47.2747 )
									ret := 0.250000
								if( tema > 47.2747 )
									ret := 0.833333 // buy
						if( ema1 > 47.3502 )
							if( tema <= 49.188 )
								if( tema <= 48.2521 )
									ret := -0.113772
								if( tema > 48.2521 )
									ret := 0.389535
							if( tema > 49.188 )
								if( ema2 <= 49.1195 )
									ret := -0.866667 // sell
								if( ema2 > 49.1195 )
									ret := -0.108696
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

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
float op_operation = decision_tree_0_AFRM_1Min_b9de3e65(ema3, tema, ema2, ema12, ema13, ema1)

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


