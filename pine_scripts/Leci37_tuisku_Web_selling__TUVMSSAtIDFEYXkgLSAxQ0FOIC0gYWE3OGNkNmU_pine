//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Candlestick_Patterns
// ID_model: MELI_1Day_1CAN_aa78cd6e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_MELI_1Day_1CAN_aa78cd6e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_MELI_1Day_aa78cd6e(Bullish_EngulfingInt, HammerInt, Evening_StarInt, Dark_Cloud_CoverInt, DojiInt, Morning_StarInt, Bearish_HaramiInt, Bullish_HaramiInt, Bullish_BeltInt, Hanging_ManInt, Bearish_EngulfingInt, Bearish_KickerInt, Piercing_LineInt, Bullish_KickerInt, Shooting_StarInt, Inverted_HammerInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=5, max_features=0.7, random_state=843828734)
	if( Bullish_KickerInt <= 0.5 )
		if( Inverted_HammerInt <= 0.5 )
			if( Morning_StarInt <= 0.5 )
				if( Evening_StarInt <= 0.5 )
					if( Bearish_EngulfingInt <= 0.5 )
						ret := -0.001432
					if( Bearish_EngulfingInt > 0.5 )
						ret := 0.194915
				if( Evening_StarInt > 0.5 )
					if( HammerInt <= 0.5 )
						ret := 0.440000
					if( HammerInt > 0.5 )
						ret := 0.750000 // buy
			if( Morning_StarInt > 0.5 )
				ret := 0.642857
		if( Inverted_HammerInt > 0.5 )
			if( Bearish_EngulfingInt <= 0.5 )
				if( Shooting_StarInt <= 0.5 )
					if( Bullish_HaramiInt <= 0.5 )
						ret := -0.205128
					if( Bullish_HaramiInt > 0.5 )
						ret := -0.647059
				if( Shooting_StarInt > 0.5 )
					ret := 0.384615
			if( Bearish_EngulfingInt > 0.5 )
				ret := 1.000000 // buy
	if( Bullish_KickerInt > 0.5 )
		if( Inverted_HammerInt <= 0.5 )
			if( DojiInt <= 0.5 )
				if( HammerInt <= 0.5 )
					if( Morning_StarInt <= 0.5 )
						ret := 0.333333
					if( Morning_StarInt > 0.5 )
						ret := 0.352941
				if( HammerInt > 0.5 )
					ret := 0.777778 // buy
			if( DojiInt > 0.5 )
				if( HammerInt <= 0.5 )
					ret := 1.000000 // buy
				if( HammerInt > 0.5 )
					ret := 0.000000
		if( Inverted_HammerInt > 0.5 )
			ret := 0.000000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Day pine_value: D   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1DAY !!"
if (str.tostring(timeframe.period) != "D")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Candlestick_Patterns 
//@version=5
//indicator title="Candles", overlay=true)

DojiSize = input.float(0.05, minval=0.01, title="Doji size")
Doji = math.abs(open - close) <= (high - low) * DojiSize
plotshape(Doji, title="Doji", color=color.white, text='Doji', style=shape.labeldown)

Evening_Star = close[2] > open[2] and math.min(open[1], close[1]) > close[2] and open < math.min(open[1], close[1]) and close < open
plotshape(Evening_Star, title="Evening_Star", color=color.red, style=shape.arrowdown, text="Evening\nStar")

Morning_Star = close[2] < open[2] and math.max(open[1], close[1]) < close[2] and open > math.max(open[1], close[1]) and close > open
plotshape(Morning_Star, title="Morning_Star", location=location.belowbar, color=color.lime, style=shape.arrowup, text="Morning\nStar")

Shooting_Star = open[1] < close[1] and open > close[1] and high - math.max(open, close) >= math.abs(open - close) * 3 and math.min(close, open) - low <= math.abs(open - close)
plotshape(Shooting_Star, title="Shooting_Star", color=color.red, style=shape.arrowdown, text="Shooting\nStar")

Hammer = (high - low) > 3 * (open - close) and (close - low) / (.001 + high - low) > 0.6 and (open - low) / (.001 + high - low) > 0.6
plotshape(Hammer, title="Hammer", location=location.belowbar, color=color.white, style=shape.diamond, text="H")

Inverted_Hammer = (high - low) > 3 * (open - close) and (high - close) / (.001 + high - low) > 0.6 and (high - open) / (.001 + high - low) > 0.6
plotshape(Inverted_Hammer, title="Inverted_Hammer", location=location.belowbar, color=color.white, style=shape.diamond, text="IH")

Bearish_Harami = close[1] > open[1] and open > close and open <= close[1] and open[1] <= close and open - close < close[1] - open[1]
plotshape(Bearish_Harami, title="Bearish_Harami", color=color.red, style=shape.arrowdown, text="Bearish\nHarami")

Bullish_Harami = open[1] > close[1] and close > open and close <= open[1] and close[1] <= open and close - open < open[1] - close[1]
plotshape(Bullish_Harami, title="Bullish_Harami", location=location.belowbar, color=color.lime, style=shape.arrowup, text="Bullish\nHarami")

Bearish_Engulfing = close[1] > open[1] and open > close and open >= close[1] and open[1] >= close and open - close > close[1] - open[1]
plotshape(Bearish_Engulfing, title="Bearish_Engulfing", color=color.red, style=shape.arrowdown, text="Bearish\nEngulfing")

Bullish_Engulfing = open[1] > close[1] and close > open and close >= open[1] and close[1] >= open and close - open > open[1] - close[1]
plotshape(Bullish_Engulfing, title="Bullish_Engulfing", location=location.belowbar, color=color.lime, style=shape.arrowup, text="Bullish\nEngulfing")

upper = ta.highest(10)[1]
Piercing_Line = close[1] < open[1] and open < low[1] and close > close[1] + (open[1] - close[1]) / 2 and close < open[1]
plotshape(Piercing_Line, title="Piercing_Line", location=location.belowbar, color=color.lime, style=shape.arrowup, text="Piercing\nLine")

lower = ta.lowest(10)[1]
Bullish_Belt = low == open and open < lower and open < close and close > (high[1] - low[1]) / 2 + low[1]
plotshape(Bullish_Belt, title="Bullish_Belt", location=location.belowbar, color=color.lime, style=shape.arrowup, text="Bullish\nBelt")

Bullish_Kicker = open[1] > close[1] and open >= open[1] and close > open
plotshape(Bullish_Kicker, title="Bullish_Kicker", location=location.belowbar, color=color.lime, style=shape.arrowup, text="Bullish\nKicker")

Bearish_Kicker = open[1] < close[1] and open <= open[1] and close <= open
plotshape(Bearish_Kicker, title="Bearish_Kicker", color=color.red, style=shape.arrowdown, text="Bearish\nKicker")

Hanging_Man = (high - low > 4 * (open - close)) and ((close - low) / (.001 + high - low) >= 0.75) and ((open - low) / (.001 + high - low) >= 0.75) and high[1] < open and high[2] < open
plotshape(Hanging_Man, title="Hanging_Man", color=color.red, style=shape.arrowdown, text="Hanging\nMan")

Dark_Cloud_Cover = close[1] > open[1] and ((close[1] + open[1]) / 2) > close and open > close and open > close[1] and close > open[1] and (open - close) / (.001 + (high - low)) > 0.6
plotshape(Dark_Cloud_Cover, title="Dark_Cloud_Cover", color=color.red, style=shape.arrowdown, text="Dark\nCloudCover")


DojiInt = Doji ? 1: 0
Evening_StarInt = Evening_Star ? 1: 0
Morning_StarInt = Morning_Star ? 1: 0
Shooting_StarInt = Shooting_Star ? 1: 0
HammerInt = Hammer ? 1: 0
Inverted_HammerInt = Inverted_Hammer ? 1: 0
Bearish_HaramiInt = Bearish_Harami ? 1: 0
Bullish_HaramiInt = Bullish_Harami ? 1: 0
Bearish_EngulfingInt = Bearish_Engulfing ? 1: 0
Bullish_EngulfingInt = Bullish_Engulfing ? 1: 0
Piercing_LineInt = Piercing_Line ? 1: 0
Bullish_BeltInt = Bullish_Belt ? 1: 0
Bullish_KickerInt = Bullish_Kicker ? 1: 0
Bearish_KickerInt = Bearish_Kicker ? 1: 0
Hanging_ManInt = Hanging_Man ? 1: 0
Dark_Cloud_CoverInt = Dark_Cloud_Cover ? 1: 0

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
float op_operation = decision_tree_0_MELI_1Day_aa78cd6e(Bullish_EngulfingInt, HammerInt, Evening_StarInt, Dark_Cloud_CoverInt, DojiInt, Morning_StarInt, Bearish_HaramiInt, Bullish_HaramiInt, Bullish_BeltInt, Hanging_ManInt, Bearish_EngulfingInt, Bearish_KickerInt, Piercing_LineInt, Bullish_KickerInt, Shooting_StarInt, Inverted_HammerInt)

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


