//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Bollinger_RSI_Double_Strategy
// ID_model: DDOG_5Min_1BOL_b66201ac Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DDOG_5Min_1BOL_b66201ac", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DDOG_5Min_b66201ac(crossunder_rsi_bbupperInt, BBlower, dif_source_BBupper, crossover_rsi_bblowerInt, vrsi, BBupper, dif_source_BBlower)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( vrsi <= 44.1704 )
		if( BBlower <= 127.735 )
			if( BBupper <= 89.6315 )
				if( dif_source_BBlower <= 1.4727 )
					if( BBupper <= 70.7178 )
						if( BBupper <= 67.1072 )
							ret := 0.806452 // buy
						if( BBupper > 67.1072 )
							ret := -0.339806
					if( BBupper > 70.7178 )
						if( BBlower <= 79.3602 )
							ret := 0.801418 // buy
						if( BBlower > 79.3602 )
							ret := 0.386423
				if( dif_source_BBlower > 1.4727 )
					if( dif_source_BBlower <= 11.5944 )
						if( dif_source_BBlower <= 9.6191 )
							ret := 0.096902
						if( dif_source_BBlower > 9.6191 )
							ret := -0.706522 // sell
					if( dif_source_BBlower > 11.5944 )
						if( vrsi <= 12.6468 )
							ret := -0.789474 // sell
						if( vrsi > 12.6468 )
							ret := 0.695652
			if( BBupper > 89.6315 )
				if( BBlower <= 90.8271 )
					if( dif_source_BBupper <= -32.6043 )
						if( BBupper <= 119.324 )
							ret := 1.000000 // buy
						if( BBupper > 119.324 )
							ret := 0.733333 // buy
					if( dif_source_BBupper > -32.6043 )
						if( vrsi <= 0.418639 )
							ret := -0.567568
						if( vrsi > 0.418639 )
							ret := -0.050330
				if( BBlower > 90.8271 )
					if( BBupper <= 96.1132 )
						if( dif_source_BBlower <= 2.36229 )
							ret := 0.389542
						if( dif_source_BBlower > 2.36229 )
							ret := -0.184211
					if( BBupper > 96.1132 )
						if( BBupper <= 134.037 )
							ret := 0.060354
						if( BBupper > 134.037 )
							ret := 0.292985
		if( BBlower > 127.735 )
			if( dif_source_BBlower <= 0.517958 )
				if( BBupper <= 136.188 )
					if( BBlower <= 129.591 )
						if( dif_source_BBupper <= -8.39861 )
							ret := 0.533333
						if( dif_source_BBupper > -8.39861 )
							ret := -0.200000
					if( BBlower > 129.591 )
						if( dif_source_BBlower <= -0.208116 )
							ret := -0.500000
						if( dif_source_BBlower > -0.208116 )
							ret := -1.000000 // sell
				if( BBupper > 136.188 )
					if( BBupper <= 137.375 )
						if( vrsi <= 11.4926 )
							ret := 0.111111
						if( vrsi > 11.4926 )
							ret := 0.927273 // buy
					if( BBupper > 137.375 )
						if( dif_source_BBlower <= -0.363032 )
							ret := 0.909091 // buy
						if( dif_source_BBlower > -0.363032 )
							ret := -0.114286
			if( dif_source_BBlower > 0.517958 )
				if( vrsi <= 17.3416 )
					if( BBupper <= 135.462 )
						if( dif_source_BBupper <= -2.59917 )
							ret := 0.437500
						if( dif_source_BBupper > -2.59917 )
							ret := -0.295775
					if( BBupper > 135.462 )
						if( BBupper <= 137.794 )
							ret := -0.842857 // sell
						if( BBupper > 137.794 )
							ret := -0.250000
				if( vrsi > 17.3416 )
					if( dif_source_BBlower <= 5.76986 )
						if( BBupper <= 131.845 )
							ret := -0.639344
						if( BBupper > 131.845 )
							ret := -0.200000
					if( dif_source_BBlower > 5.76986 )
						if( vrsi <= 31.9629 )
							ret := 1.000000 // buy
						if( vrsi > 31.9629 )
							ret := 0.076923
	if( vrsi > 44.1704 )
		if( dif_source_BBlower <= 4.85729 )
			if( dif_source_BBlower <= 1.64609 )
				if( BBupper <= 136.173 )
					if( BBupper <= 134.535 )
						if( BBupper <= 132.747 )
							ret := 0.025381
						if( BBupper > 132.747 )
							ret := 0.401747
					if( BBupper > 134.535 )
						if( BBupper <= 135.442 )
							ret := -0.544379
						if( BBupper > 135.442 )
							ret := 0.088889
				if( BBupper > 136.173 )
					if( vrsi <= 49.5864 )
						if( BBupper <= 137.851 )
							ret := 0.100000
						if( BBupper > 137.851 )
							ret := -0.692308
					if( vrsi > 49.5864 )
						if( dif_source_BBupper <= -4.82364 )
							ret := 0.724771 // buy
						if( dif_source_BBupper > -4.82364 )
							ret := 0.055556
			if( dif_source_BBlower > 1.64609 )
				if( dif_source_BBupper <= 0.002868 )
					if( BBupper <= 66.8597 )
						if( dif_source_BBupper <= -0.140646 )
							ret := 0.826923 // buy
						if( dif_source_BBupper > -0.140646 )
							ret := -0.250000
					if( BBupper > 66.8597 )
						if( BBupper <= 134.286 )
							ret := -0.047571
						if( BBupper > 134.286 )
							ret := -0.291667
				if( dif_source_BBupper > 0.002868 )
					if( BBlower <= 85.1306 )
						if( dif_source_BBupper <= 0.084376 )
							ret := 0.000000
						if( dif_source_BBupper > 0.084376 )
							ret := -0.727273 // sell
					if( BBlower > 85.1306 )
						if( BBupper <= 122.035 )
							ret := 0.204170
						if( BBupper > 122.035 )
							ret := -0.163205
		if( dif_source_BBlower > 4.85729 )
			if( vrsi <= 84.849 )
				if( dif_source_BBlower <= 36.5191 )
					if( dif_source_BBupper <= 1.86743 )
						if( BBupper <= 119.385 )
							ret := -0.174331
						if( BBupper > 119.385 )
							ret := -0.045171
					if( dif_source_BBupper > 1.86743 )
						if( dif_source_BBupper <= 4.35469 )
							ret := 0.463519
						if( dif_source_BBupper > 4.35469 )
							ret := -0.625000
				if( dif_source_BBlower > 36.5191 )
					ret := -1.000000 // sell
			if( vrsi > 84.849 )
				if( dif_source_BBlower <= 6.5104 )
					if( dif_source_BBupper <= -0.969268 )
						if( dif_source_BBupper <= -9.7456 )
							ret := 0.750000 // buy
						if( dif_source_BBupper > -9.7456 )
							ret := -0.502762
					if( dif_source_BBupper > -0.969268 )
						if( BBupper <= 110.009 )
							ret := 0.258929
						if( BBupper > 110.009 )
							ret := -0.181373
				if( dif_source_BBlower > 6.5104 )
					if( BBupper <= 71.2598 )
						if( dif_source_BBupper <= 2.25544 )
							ret := -0.333333
						if( dif_source_BBupper > 2.25544 )
							ret := 0.941176 // buy
					if( BBupper > 71.2598 )
						if( dif_source_BBupper <= -4.09372 )
							ret := -0.225806
						if( dif_source_BBupper > -4.09372 )
							ret := -0.630282
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Bollinger_RSI_Double_Strategy 
//@version=5
//strategy "Bollinger + RSI, Double Strategy (by ChartArt) v1.1", shorttitle="CA_-_RSI_Bol_Strat_1.1", overlay=true)

// ChartArt's RSI + Bollinger Bands, Double Strategy - Update
//
// Version 1.1
// Idea by ChartArt on January 18, 2015.
//
// This strategy uses the RSI indicator
// together with the Bollinger Bands
// to sell when the price is above the
// upper Bollinger Band (and to buy when
// this value is below the lower band).
//
// This simple strategy only triggers when
// both the RSI and the Bollinger Bands
// indicators are at the same time in
// a overbought or oversold condition.
//
// In this version 1.1 the strategy was
// both simplified for the user and
// made more successful in backtesting.
//
// List of my work:
// https://www.tradingview.com/u/ChartArt/
//
//  __             __  ___       __  ___
// /  ` |__|  /\  |__)  |   /\  |__)  |
// \__, |  | /~~\ |  \  |  /~~\ |  \  |
//
//

///////////// RSI
RSIlength = input.int(6, title="RSI Period Length")
RSIoverSold = 50
RSIoverBought = 50
price = close
vrsi = ta.rsi(price, RSIlength)

///////////// Bollinger Bands
BBlength = input.int(200, minval=1, title="Bollinger Period Length")
BBmult = 2 // input(2.0, minval=0.001, maxval=50,title="Bollinger Bands Standard Deviation")
BBbasis = ta.sma(price, BBlength)
BBdev = BBmult * ta.stdev(price, BBlength)
BBupper = BBbasis + BBdev
BBlower = BBbasis - BBdev
source = close
buyEntry = ta.crossover(source, BBlower)
sellEntry = ta.crossunder(source, BBupper)
plot(BBbasis, color=color.aqua, title="Bollinger Bands SMA Basis Line")
p1 = plot(BBupper, color=color.silver, title="Bollinger Bands Upper Line")
p2 = plot(BBlower, color=color.silver, title="Bollinger Bands Lower Line")
fill(p1, p2)

///////////// Colors
switch1 = input(true, title="Enable Bar Color?")
switch2 = input(true, title="Enable Background Color?")
TrendColor = (price[1] > BBupper and price < BBupper and BBbasis < BBbasis[1]) ? color.red : (price[1] < BBlower and price > BBlower and BBbasis > BBbasis[1]) ? color.green : na
// bgColor1 = color.new(TrendColor, 70)
barcolor(switch1 ? TrendColor : na)

// Using color.new() to set transparency
bgColor = color.new(TrendColor, 90)
bgcolor(switch2 ? bgColor : na)

///////////// RSI + Bollinger Bands Strategy
crossover_rsi_bblower = ta.crossover(vrsi, RSIoverSold) and ta.crossover(source, BBlower)
crossunder_rsi_bbupper = ta.crossunder(vrsi, RSIoverBought) and ta.crossunder(source, BBupper)

crossover_rsi_bblowerInt = crossover_rsi_bblower ? 1: 0    //Bool to int
crossunder_rsi_bbupperInt = crossunder_rsi_bbupper ? 1: 0  //Bool to int

dif_vrsi_RSIoverSold = vrsi - RSIoverSold
dif_source_BBlower = source - BBlower
dif_vrsi_RSIoverBought = vrsi - RSIoverBought
dif_source_BBupper = source - BBupper

// if not na(vrsi)
//     if crossover_rsi_bblower
//         strategy.entry("RSI_BB_L", strategy.long, stop=BBlower, oca_type=strategy.oca.cancel, comment="RSI_BB_L")
//     else
//         strategy.cancel(id="RSI_BB_L")
//
//     if crossunder_rsi_bbupper
//         strategy.entry("RSI_BB_S", strategy.short, stop=BBupper, oca_type=strategy.oca.cancel, comment="RSI_BB_S")
//     else
//         strategy.cancel(id="RSI_BB_S")

//plot(strategy.equity, title="equity", color=color.red, linewidth=2, style=plot.style_areabr)
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
float op_operation = decision_tree_0_DDOG_5Min_b66201ac(crossunder_rsi_bbupperInt, BBlower, dif_source_BBupper, crossover_rsi_bblowerInt, vrsi, BBupper, dif_source_BBlower)

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


