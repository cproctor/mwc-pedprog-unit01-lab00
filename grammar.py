from vocabulary import starts_with_vowel_sound
from grammatical_types import (
    Adjective,
    Adverb, 
    DeterminedNounPhrase,
    Determiner, 
    IntransitiveVerb,
    Noun, 
    NounPhrase,
    PastTenseTransitiveVerb,
    PastTenseIntransitiveVerb,
    PluralNoun,
    Sentence,
    TransitiveVerb,
    VerbPhrase, 
)

def pluralize(noun):
    "Noun -> PluralNoun"
    assert type(noun) == Noun
    if noun.endswith("s") or noun.endswith("ch") or noun.endswith("sh") or noun.endswith("x"):
        return PluralNoun(noun + 'es')
    else:
        return PluralNoun(noun + 's')

def noun_phrase(adjective, noun):
    "(Adjective, Noun) -> NounPhrase"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def determine_noun_phrase(determiner, noun_phrase):
    "(Determiner, NounPhrase) -> Determined NounPhrase"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def make_definite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def make_indefinite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def verb_phrase(adverb, verb_phrase):
    "(Adverb, VerbPhrase) -> VerbPhrase"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def past_tense_transitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def past_tense_intransitive(verb):
    "TransitiveVerb -> PastTenseIntransitiveVerb"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

def verb_phrase_transitive(verb, noun_phrase):
    "(TransitiveVerb, NounPhrase) -> VerbPhrase"
    #YOUR CODE GOES HERE
    raise NotImplementedError("This function isn't done!")

