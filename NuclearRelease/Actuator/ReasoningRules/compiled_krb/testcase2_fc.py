# testcase2_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.0.4'
compiler_version = 1

def has_intention_to(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'int_status', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'has_intention',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_intention_that(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'int_status', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'has_intention',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def parent_of_action(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'subaction_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'parent_of',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def parent_of_parameter(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'param_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'parent_of',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ancestor_of_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'parent_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'ancestor_of',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ancestor_of_grand(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'parent_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'parent_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('plangraph', 'ancestor_of',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ancestor_of_ancestor(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'parent_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'ancestor_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('plangraph', 'ancestor_of',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def belief_value_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'has_intention', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'ancestor_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('plangraph', 'value_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('plangraph', 'generated_value_of', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('value1') == context.lookup_data('value2'):
                      engine.assert_('plangraph', 'belief_value_of',
                                     (rule.pattern(0).as_data(context),
                                      rule.pattern(1).as_data(context),
                                      rule.pattern(2).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def inform_belief_value_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'belief_value_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('plangraph', 'param_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('plangraph', 'status_of', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('status1') != 'exec_success':
                      with knowledge_base.Gen_once if index == 4 \
                               else engine.lookup('plangraph', 'status_of', context,
                                                  rule.foreach_patterns(4)) \
                        as gen_4:
                        for dummy in gen_4:
                          if context.lookup_data('status2') != 'param_status_success':
                            engine.assert_('maprole', 'inform_belief_value_of',
                                           (rule.pattern(0).as_data(context),
                                            rule.pattern(1).as_data(context),
                                            rule.pattern(2).as_data(context),)),
                            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def contextualize_action(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'has_intention', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'context_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('plangraph', 'status_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('status') != 'exec_success':
                  engine.assert_('maprole', 'contextualize_action',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def show_mb_value_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'param_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'status_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status1') != 'exec_success':
              with knowledge_base.Gen_once if index == 2 \
                       else engine.lookup('plangraph', 'status_of', context,
                                          rule.foreach_patterns(2)) \
                as gen_2:
                for dummy in gen_2:
                  with knowledge_base.Gen_once if index == 3 \
                           else engine.lookup('plangraph', 'value_of', context,
                                              rule.foreach_patterns(3)) \
                    as gen_3:
                    for dummy in gen_3:
                      with knowledge_base.Gen_once if index == 4 \
                               else engine.lookup('geocontent', 'type_of', context,
                                                  rule.foreach_patterns(4)) \
                        as gen_4:
                        for dummy in gen_4:
                          engine.assert_('maprole', 'show_mb_value_of',
                                         (rule.pattern(0).as_data(context),
                                          rule.pattern(1).as_data(context),)),
                          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def show_subaction_value_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'subaction_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('plangraph', 'status_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('status1') != 'exec_success':
                  with knowledge_base.Gen_once if index == 3 \
                           else engine.lookup('plangraph', 'status_of', context,
                                              rule.foreach_patterns(3)) \
                    as gen_3:
                    for dummy in gen_3:
                      with knowledge_base.Gen_once if index == 4 \
                               else engine.lookup('plangraph', 'generated_value_of', context,
                                                  rule.foreach_patterns(4)) \
                        as gen_4:
                        for dummy in gen_4:
                          with knowledge_base.Gen_once if index == 5 \
                                   else engine.lookup('geocontent', 'type_of', context,
                                                      rule.foreach_patterns(5)) \
                            as gen_5:
                            for dummy in gen_5:
                              engine.assert_('maprole', 'show_subaction_value_of',
                                             (rule.pattern(0).as_data(context),
                                              rule.pattern(1).as_data(context),)),
                              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'inform_belief_value_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('maptask', 'locate',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def emphasize(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'inform_belief_value_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('type') != 'layer':
              if context.lookup_data('type') != 'location':
                engine.assert_('maptask', 'emphasize',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def background(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'contextualize_action', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('maptask', 'background',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def foreground_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'contextualize_action', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('type') != 'layer':
              engine.assert_('maptask', 'foreground',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def foreground_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'show_mb_value_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('type') != 'layer':
              engine.assert_('maptask', 'foreground',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def foreground_3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'show_subaction_value_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('type') != 'layer':
              engine.assert_('maptask', 'foreground',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate_stra_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'locate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_1',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_1',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(6).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate_stra_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'locate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_2',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_2',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(6).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_2',
                       (rule.pattern(7).as_data(context),
                        rule.pattern(6).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate_stra_3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'locate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_3',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_3',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(6).as_data(context),)),
        engine.assert_('mapstra', 'locate_stra_3',
                       (rule.pattern(7).as_data(context),
                        rule.pattern(6).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def emphasize_stra_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'emphasize', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'emphasize_stra_1',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'emphasize_stra_1',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def emphasize_stra_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'emphasize', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'emphasize_stra_2',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'emphasize_stra_2',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def background_stra(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'background', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'background_stra',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def foreground_stra_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'foreground', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'foreground_stra_1',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'foreground_stra_1',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def foreground_stra_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'foreground', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapstra', 'fulfill',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        engine.assert_('mapstra', 'foreground_stra_2',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        engine.assert_('mapstra', 'foreground_stra_2',
                       (rule.pattern(5).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('testcase2')
  
  fc_rule.fc_rule('has_intention_to', This_rule_base, has_intention_to,
    (('plangraph', 'int_status',
      (contexts.variable('agent'),
       contexts.variable('action'),
       pattern.pattern_literal('int_intendTo'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('action'),))
  
  fc_rule.fc_rule('has_intention_that', This_rule_base, has_intention_that,
    (('plangraph', 'int_status',
      (contexts.variable('agent'),
       contexts.variable('action'),
       pattern.pattern_literal('int_intendThat'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('action'),))
  
  fc_rule.fc_rule('parent_of_action', This_rule_base, parent_of_action,
    (('plangraph', 'subaction_of',
      (contexts.variable('subaction'),
       contexts.variable('plannode'),),
      False),),
    (contexts.variable('plannode'),
     contexts.variable('subaction'),))
  
  fc_rule.fc_rule('parent_of_parameter', This_rule_base, parent_of_parameter,
    (('plangraph', 'param_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('action'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('ancestor_of_parent', This_rule_base, ancestor_of_parent,
    (('plangraph', 'parent_of',
      (contexts.variable('parent'),
       contexts.variable('son'),),
      False),),
    (contexts.variable('parent'),
     contexts.variable('son'),))
  
  fc_rule.fc_rule('ancestor_of_grand', This_rule_base, ancestor_of_grand,
    (('plangraph', 'parent_of',
      (contexts.variable('parent'),
       contexts.variable('son'),),
      False),
     ('plangraph', 'parent_of',
      (contexts.variable('grand'),
       contexts.variable('parent'),),
      False),),
    (contexts.variable('grand'),
     contexts.variable('son'),))
  
  fc_rule.fc_rule('ancestor_of_ancestor', This_rule_base, ancestor_of_ancestor,
    (('plangraph', 'parent_of',
      (contexts.variable('parent'),
       contexts.variable('son'),),
      False),
     ('plangraph', 'ancestor_of',
      (contexts.variable('ancestor'),
       contexts.variable('parent'),),
      False),),
    (contexts.variable('ancestor'),
     contexts.variable('son'),))
  
  fc_rule.fc_rule('belief_value_of', This_rule_base, belief_value_of,
    (('plangraph', 'has_intention',
      (contexts.variable('agent'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'ancestor_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'value_of',
      (contexts.variable('value1'),
       contexts.variable('param'),),
      False),
     ('plangraph', 'generated_value_of',
      (contexts.variable('value2'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('value1'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('inform_belief_value_of', This_rule_base, inform_belief_value_of,
    (('plangraph', 'belief_value_of',
      (contexts.variable('agent'),
       contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (contexts.anonymous('_'),
       contexts.variable('value'),),
      False),
     ('plangraph', 'param_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status1'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status2'),
       contexts.variable('param'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('value'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('contextualize_action', This_rule_base, contextualize_action,
    (('plangraph', 'has_intention',
      (contexts.variable('agent'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'context_of',
      (contexts.variable('value'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('value'),
     contexts.variable('action'),))
  
  fc_rule.fc_rule('show_mb_value_of', This_rule_base, show_mb_value_of,
    (('plangraph', 'param_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status1'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (pattern.pattern_literal('param_status_success'),
       contexts.variable('param'),),
      False),
     ('plangraph', 'value_of',
      (contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (contexts.anonymous('_'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('show_subaction_value_of', This_rule_base, show_subaction_value_of,
    (('plangraph', 'subaction_of',
      (contexts.variable('subaction'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'type_of',
      (pattern.pattern_literal('action'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status1'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (pattern.pattern_literal('exec_success'),
       contexts.variable('subaction'),),
      False),
     ('plangraph', 'generated_value_of',
      (contexts.variable('value'),
       contexts.variable('subaction'),),
      False),
     ('geocontent', 'type_of',
      (contexts.anonymous('_'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     contexts.variable('subaction'),))
  
  fc_rule.fc_rule('locate', This_rule_base, locate,
    (('maprole', 'inform_belief_value_of',
      (contexts.variable('agent'),
       contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (pattern.pattern_literal('location'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     pattern.pattern_literal('The map is to inform other users of this location'),))
  
  fc_rule.fc_rule('emphasize', This_rule_base, emphasize,
    (('maprole', 'inform_belief_value_of',
      (contexts.variable('agent'),
       contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (contexts.variable('type'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     pattern.pattern_literal('The map is to inform other users about your belief of the value'),))
  
  fc_rule.fc_rule('background', This_rule_base, background,
    (('maprole', 'contextualize_action',
      (contexts.variable('value'),
       contexts.variable('action'),),
      False),
     ('geocontent', 'type_of',
      (pattern.pattern_literal('layer'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     pattern.pattern_literal('The map provides relevant contextual layers about the current activity'),))
  
  fc_rule.fc_rule('foreground_1', This_rule_base, foreground_1,
    (('maprole', 'contextualize_action',
      (contexts.variable('value'),
       contexts.variable('action'),),
      False),
     ('geocontent', 'type_of',
      (contexts.variable('type'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     pattern.pattern_literal('The map provides relevant contextual features about the current activity'),))
  
  fc_rule.fc_rule('foreground_2', This_rule_base, foreground_2,
    (('maprole', 'show_mb_value_of',
      (contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (contexts.variable('type'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     pattern.pattern_literal('The map shows the value of parameter that has been mutually believed by the group'),))
  
  fc_rule.fc_rule('foreground_3', This_rule_base, foreground_3,
    (('maprole', 'show_subaction_value_of',
      (contexts.variable('value'),
       contexts.variable('action'),),
      False),
     ('geocontent', 'type_of',
      (contexts.variable('type'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),
     pattern.pattern_literal('The map shows the value generated by an action'),))
  
  fc_rule.fc_rule('locate_stra_1', This_rule_base, locate_stra_1,
    (('maptask', 'locate',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('locate_stra_1'),
     pattern.pattern_literal('locate'),
     pattern.pattern_literal("The map shows at the state-level scale, so that the users can identify the location relative to the belonging State"),
     pattern.pattern_literal('scale_level'),
     pattern.pattern_literal('state'),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('locate_stra_2', This_rule_base, locate_stra_2,
    (('maptask', 'locate',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('locate_stra_2'),
     pattern.pattern_literal('locate'),
     pattern.pattern_literal("The map shows the location in the local detail and center to the location to raise user's attention"),
     pattern.pattern_literal('scale_level'),
     pattern.pattern_literal('local'),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),
     pattern.pattern_literal('center'),))
  
  fc_rule.fc_rule('locate_stra_3', This_rule_base, locate_stra_3,
    (('maptask', 'locate',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('locate_stra_3'),
     pattern.pattern_literal('locate'),
     pattern.pattern_literal("The map shows at the county-level scale and center to the location, so that the users can see the relevant context around the location"),
     pattern.pattern_literal('scale_level'),
     pattern.pattern_literal('county'),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),
     pattern.pattern_literal('center'),))
  
  fc_rule.fc_rule('emphasize_stra_1', This_rule_base, emphasize_stra_1,
    (('maptask', 'emphasize',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('emphasize_stra_1'),
     pattern.pattern_literal('emphasize'),
     pattern.pattern_literal("The map emphasize the object by highlighting the boundary"),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),
     pattern.pattern_literal('highlight'),))
  
  fc_rule.fc_rule('emphasize_stra_2', This_rule_base, emphasize_stra_2,
    (('maptask', 'emphasize',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('emphasize_stra_2'),
     pattern.pattern_literal('emphasize'),
     pattern.pattern_literal("The map emphasize the object by putting the object at the center of map view"),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),
     pattern.pattern_literal('center'),))
  
  fc_rule.fc_rule('background_stra', This_rule_base, background_stra,
    (('maptask', 'background',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('background_stra'),
     pattern.pattern_literal('background'),
     pattern.pattern_literal('The map will add the relevant layers as background layers.'),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('foreground_stra_1', This_rule_base, foreground_stra_1,
    (('maptask', 'foreground',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('foreground_stra_1'),
     pattern.pattern_literal('foreground'),
     pattern.pattern_literal('The map scale must be adjusted so that all the relevant features are visible'),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),
     pattern.pattern_literal('visible'),))
  
  fc_rule.fc_rule('foreground_stra_2', This_rule_base, foreground_stra_2,
    (('maptask', 'foreground',
      (contexts.variable('value'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('foreground_stra_2'),
     pattern.pattern_literal('foreground'),
     pattern.pattern_literal('The map scale must be adjusted so that not only the relevant features, but also surrounding contexts are visible'),
     pattern.pattern_literal('layer'),
     contexts.variable('value'),
     pattern.pattern_literal('visible_in_context'),))


Krb_filename = '../testcase2.krb'
Krb_lineno_map = (
    ((13, 17), (4, 4)),
    ((18, 20), (6, 6)),
    ((29, 33), (10, 10)),
    ((34, 36), (12, 12)),
    ((45, 49), (16, 16)),
    ((50, 52), (18, 18)),
    ((61, 65), (22, 22)),
    ((66, 68), (24, 24)),
    ((77, 81), (28, 28)),
    ((82, 84), (30, 30)),
    ((93, 97), (34, 34)),
    ((98, 102), (35, 35)),
    ((103, 105), (37, 37)),
    ((114, 118), (41, 41)),
    ((119, 123), (42, 42)),
    ((124, 126), (44, 44)),
    ((135, 139), (48, 48)),
    ((140, 144), (49, 49)),
    ((145, 149), (50, 50)),
    ((150, 154), (51, 51)),
    ((155, 155), (52, 52)),
    ((156, 159), (54, 54)),
    ((168, 172), (59, 59)),
    ((173, 177), (60, 60)),
    ((178, 182), (61, 61)),
    ((183, 187), (62, 62)),
    ((188, 188), (63, 63)),
    ((189, 193), (64, 64)),
    ((194, 194), (65, 65)),
    ((195, 198), (67, 67)),
    ((207, 211), (71, 71)),
    ((212, 216), (72, 72)),
    ((217, 221), (73, 73)),
    ((222, 222), (74, 74)),
    ((223, 225), (76, 76)),
    ((234, 238), (80, 80)),
    ((239, 243), (81, 81)),
    ((244, 244), (82, 82)),
    ((245, 249), (83, 83)),
    ((250, 254), (84, 84)),
    ((255, 259), (85, 85)),
    ((260, 262), (87, 87)),
    ((271, 275), (91, 91)),
    ((276, 280), (92, 92)),
    ((281, 285), (93, 93)),
    ((286, 286), (94, 94)),
    ((287, 291), (95, 95)),
    ((292, 296), (96, 96)),
    ((297, 301), (97, 97)),
    ((302, 304), (99, 99)),
    ((313, 317), (104, 104)),
    ((318, 322), (105, 105)),
    ((323, 325), (107, 107)),
    ((334, 338), (111, 111)),
    ((339, 343), (112, 112)),
    ((344, 344), (113, 113)),
    ((345, 345), (114, 114)),
    ((346, 348), (116, 116)),
    ((357, 361), (120, 120)),
    ((362, 366), (121, 121)),
    ((367, 369), (123, 123)),
    ((378, 382), (127, 127)),
    ((383, 387), (128, 128)),
    ((388, 388), (129, 129)),
    ((389, 391), (131, 131)),
    ((400, 404), (135, 135)),
    ((405, 409), (136, 136)),
    ((410, 410), (137, 137)),
    ((411, 413), (139, 139)),
    ((422, 426), (143, 143)),
    ((427, 431), (144, 144)),
    ((432, 432), (145, 145)),
    ((433, 435), (147, 147)),
    ((444, 448), (152, 152)),
    ((449, 452), (154, 154)),
    ((453, 455), (155, 155)),
    ((456, 458), (156, 156)),
    ((467, 471), (160, 160)),
    ((472, 475), (162, 162)),
    ((476, 478), (163, 163)),
    ((479, 481), (164, 164)),
    ((482, 484), (165, 165)),
    ((493, 497), (169, 169)),
    ((498, 501), (171, 171)),
    ((502, 504), (172, 172)),
    ((505, 507), (173, 173)),
    ((508, 510), (174, 174)),
    ((519, 523), (178, 178)),
    ((524, 527), (180, 180)),
    ((528, 530), (181, 181)),
    ((531, 533), (182, 182)),
    ((542, 546), (186, 186)),
    ((547, 550), (188, 188)),
    ((551, 553), (189, 189)),
    ((554, 556), (190, 190)),
    ((565, 569), (194, 194)),
    ((570, 573), (196, 196)),
    ((574, 576), (197, 197)),
    ((585, 589), (201, 201)),
    ((590, 593), (203, 203)),
    ((594, 596), (204, 204)),
    ((597, 599), (205, 205)),
    ((608, 612), (209, 209)),
    ((613, 616), (211, 211)),
    ((617, 619), (212, 212)),
    ((620, 622), (213, 213)),
)
