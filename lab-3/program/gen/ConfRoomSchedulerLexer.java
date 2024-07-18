// Generated from ConfRoomScheduler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ConfRoomSchedulerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, DATE=6, TIME=7, ID=8, NEWLINE=9, 
		WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "DATE", "TIME", "ID", "NEWLINE", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'RESERVAR'", "'PARA'", "'DE'", "'A'", "'CANCELAR'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "DATE", "TIME", "ID", "NEWLINE", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ConfRoomSchedulerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ConfRoomScheduler.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 5:
			DATE_action((RuleContext)_localctx, actionIndex);
			break;
		case 6:
			TIME_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void DATE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			2
			break;
		case 1:
			2
			break;
		case 2:
			4
			break;
		}
	}
	private void TIME_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			2
			break;
		case 4:
			2
			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000\nQ\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0004"+
		"\u0007B\b\u0007\u000b\u0007\f\u0007C\u0001\b\u0003\bG\b\b\u0001\b\u0001"+
		"\b\u0001\t\u0004\tL\b\t\u000b\t\f\tM\u0001\t\u0001\t\u0000\u0000\n\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0001\u0000\u0003\u0001\u000009\u0003\u00000"+
		"9AZaz\u0002\u0000\t\t  S\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0001\u0015\u0001\u0000\u0000\u0000\u0003\u001e\u0001\u0000"+
		"\u0000\u0000\u0005#\u0001\u0000\u0000\u0000\u0007&\u0001\u0000\u0000\u0000"+
		"\t(\u0001\u0000\u0000\u0000\u000b1\u0001\u0000\u0000\u0000\r:\u0001\u0000"+
		"\u0000\u0000\u000fA\u0001\u0000\u0000\u0000\u0011F\u0001\u0000\u0000\u0000"+
		"\u0013K\u0001\u0000\u0000\u0000\u0015\u0016\u0005R\u0000\u0000\u0016\u0017"+
		"\u0005E\u0000\u0000\u0017\u0018\u0005S\u0000\u0000\u0018\u0019\u0005E"+
		"\u0000\u0000\u0019\u001a\u0005R\u0000\u0000\u001a\u001b\u0005V\u0000\u0000"+
		"\u001b\u001c\u0005A\u0000\u0000\u001c\u001d\u0005R\u0000\u0000\u001d\u0002"+
		"\u0001\u0000\u0000\u0000\u001e\u001f\u0005P\u0000\u0000\u001f \u0005A"+
		"\u0000\u0000 !\u0005R\u0000\u0000!\"\u0005A\u0000\u0000\"\u0004\u0001"+
		"\u0000\u0000\u0000#$\u0005D\u0000\u0000$%\u0005E\u0000\u0000%\u0006\u0001"+
		"\u0000\u0000\u0000&\'\u0005A\u0000\u0000\'\b\u0001\u0000\u0000\u0000("+
		")\u0005C\u0000\u0000)*\u0005A\u0000\u0000*+\u0005N\u0000\u0000+,\u0005"+
		"C\u0000\u0000,-\u0005E\u0000\u0000-.\u0005L\u0000\u0000./\u0005A\u0000"+
		"\u0000/0\u0005R\u0000\u00000\n\u0001\u0000\u0000\u000012\u0007\u0000\u0000"+
		"\u000023\u0006\u0005\u0000\u000034\u0005/\u0000\u000045\u0007\u0000\u0000"+
		"\u000056\u0006\u0005\u0001\u000067\u0005/\u0000\u000078\u0007\u0000\u0000"+
		"\u000089\u0006\u0005\u0002\u00009\f\u0001\u0000\u0000\u0000:;\u0007\u0000"+
		"\u0000\u0000;<\u0006\u0006\u0003\u0000<=\u0005:\u0000\u0000=>\u0007\u0000"+
		"\u0000\u0000>?\u0006\u0006\u0004\u0000?\u000e\u0001\u0000\u0000\u0000"+
		"@B\u0007\u0001\u0000\u0000A@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000"+
		"\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000D\u0010\u0001"+
		"\u0000\u0000\u0000EG\u0005\r\u0000\u0000FE\u0001\u0000\u0000\u0000FG\u0001"+
		"\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0005\n\u0000\u0000I\u0012"+
		"\u0001\u0000\u0000\u0000JL\u0007\u0002\u0000\u0000KJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000"+
		"\u0000\u0000NO\u0001\u0000\u0000\u0000OP\u0006\t\u0005\u0000P\u0014\u0001"+
		"\u0000\u0000\u0000\u0004\u0000CFM\u0006\u0001\u0005\u0000\u0001\u0005"+
		"\u0001\u0001\u0005\u0002\u0001\u0006\u0003\u0001\u0006\u0004\u0006\u0000"+
		"\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}